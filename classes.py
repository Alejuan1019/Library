import os
import copy
print(os.getcwd())


class Error(Exception):
    pass


class Book:
    inventory = []
    total_sales = {}

    def __init__(self, title: str, category: str, ID: str, price: float, quantity=1, ):
        self.title = title
        self.category = category
        self.ID = ID
        self.price = price
        self.quantity = quantity
        Book.inventory.append(self)

    def sold_book(self, num: int):
        if num <= self.quantity > 0:
            total_price = num * self.price
            self.quantity = self.quantity - num
            print(f"You have purchased {str(num)} copy/s of {self.title.title()} for {str(total_price)}")
            Book.add_sale(self, num, total_price)
        elif self.quantity == 0:
            Error(f"Sorry, we don't have any available copy for {self.title.title()}")
        elif self.quantity > 1:
            Error(f"Sorry, {self.title.title()}, has only {str(self.quantity)} copies available ")
        else:
            Error(f"Sorry, {self.title.title()}, has only 1 copy available ")

    def edit_book(self):
        while True:
            choice = input("What do you want to edit? Type which one you want to edit (Title/Category/ID/Price/Quantity) \
            or type (see) to see the book's details type (quit) to exit: ").lower().strip()
            if choice == 'title':
                print(f"\nUpdate {self.title.title()}'s title")
                new_title = input("\nWhat is the new title? ").lower().strip()
                old_title = copy.deepcopy(self.title)
                self.title = new_title
                print(f"\n'{old_title.title()}' has changed to '{self.title.title()}'")
            elif choice == 'category':
                print(f"\n{self.title.title()}'s current category is {self.category.title()}")
                new_category = input("\nWhat is the new category for this book? ").lower().strip()
                old_category = copy.deepcopy(self.category)
                self.category = new_category
                print(f"\n{self.title.title()}'s category has changed from {old_category.title()} to {self.category.title()}")
            elif choice == 'id':
                print(f"\n{self.title.title()}'s current ID is {self.ID}")
                new_ID = input("\nWhat is the new ID for this book? ").lower().strip()
                old_ID = copy.deepcopy(self.ID)
                self.ID = new_ID
                print(f"\n{self.title.title()}'s ID has changed from {old_ID} to {self.ID}")
            elif choice == 'price':
                print(f"{self.title.title()}'s current price is £{self.price:.2f}")
                new_price = Book.price_set()
                old_price = copy.deepcopy(self.price)
                self.price = new_price
                print(f"\n{self.title.title()}'s price has changed from £{old_price:.2f} has changed to £{self.price:.2f}")
            elif choice == 'see':
                print(f"Title: {self.title.title()}, Category: {self.category.title()}, ID: {self.ID}, price: £{self.price}, quantity: {self.quantity}\n")
            elif choice == 'quit':
                return
            elif choice == 'quantity':
                while True:
                    print(f"{self.title.title()}'s current quantity in stock is {str(self.quantity)}")
                    choice = input("\nDo you want to add more books (press 1) or edit the quantity of books (press 2): ").lower().strip()
                    if choice == '1':
                        while True:
                            add = input("\nHow many books do you want to add: ")
                            if add.isnumeric():
                                new_qty = int(self.quantity) + int(add)
                                self.quantity = new_qty
                                print(
                                    f"\n {add} book/s have been added and the new quantity in stock for {self.title.title()} is {str(self.quantity)}")
                                return
                            else:
                                print("(Please type a valid quantity)")
                    elif choice == '2':
                        print(f"\nUpdating {self.title.title()}'s quantity")
                        while True:
                            new_qty = input(f"\nHWhat is the new quantity for {self.title.title()}: ")
                            if new_qty.isnumeric():
                                self.quantity = new_qty
                                print(f"\n {self.title.title()}'s new quantity is {str(self.quantity)}")
                                return
                            else:
                                print("(Please type a valid quantity)")
                    else:
                        print("Type 1 or 2")
            else:
                print("(please select a valid option: title, category, ID, price, quantity or quit)")

    @classmethod
    def add_sale(cls, book_sold, number_sold, income):
        if book_sold.title in cls.total_sales:
            old_quantity_sold = cls.total_sales[book_sold.title]['qty_sold']
            new_quantity_sold = old_quantity_sold + number_sold
            cls.total_sales[book_sold.title]['qty_sold'] = new_quantity_sold
            old_income = cls.total_sales[book_sold.title]['total_income']
            new_income = old_income + income
            cls.total_sales[book_sold.title]['total_income'] = new_income
        else:
            cls.total_sales[book_sold.title] = {'qty_sold': number_sold, 'total_income': income}

    @classmethod
    def add_new_book(cls, title=None, ID=None):
        if title is None:
            title = input("What is the tittle of the new book? ").lower().strip()
            ID = input("What is the book's ID? ").strip()
        category = input("What it's the book category? ").lower().strip()
        price = cls.price_set()
        while True:
            quantity = input("How many books are you adding to the system? ")
            if quantity.isdigit():
                quantity = int(quantity)
                break
            else:
                print("(Please type a valid quantity)")
        book_instance = Book(title, category, ID, price, quantity)
        print("\nThe following has been added to the inventory")
        print(f"(Book: {title.title()}  |  Category: {category.title()}  |  ID: {ID}  |  Price: £{float(price):.2f}  |  Quantity: {str(quantity)})")
        return

    @classmethod
    def check_for_book(cls):
        title = input("\nWhat is the tittle of the book? ").lower().strip()
        list_of_titles = [i.title for i in cls.inventory]
        match = list_of_titles.count(title)
        if match > 0:
            print(f"Book already exists with this title. Accessing existing book to edit...")
            return True, 'title', title

        else:
            print("(Book was not found by title search)")
            ID = input("\nWhat is the book's ID? ").strip()
            list_of_ids = [i.ID for i in cls.inventory]
            match = list_of_ids.count(ID)
            if match > 0:
                print(f"Book already exists with this ID. Accessing existing book to edit...")
                return True, 'ID', ID
            else:
                return False, title, ID

    @classmethod
    def get_book(cls, found_by, title_id):
        if found_by == 'ID':
            list_of_ids = [i.ID for i in cls.inventory]
            book_location = list_of_ids.index(title_id)
            item = cls.inventory[book_location]
            print("The following book has been found\n")
            print(
                f"Title: {item.title.title()}, Category: {item.category.title()}, ID: {item.ID}, price: £{item.price}, quantity: {item.quantity}\n")
            return item
        elif found_by == 'title':
            list_of_titles = [i.title for i in cls.inventory]
            book_location = list_of_titles.index(title_id)
            item = cls.inventory[book_location]
            print("The following book has been found\n")
            print(
                f"Title: {item.title.title()}, Category: {item.category.title()}, ID: {item.ID}, price: £{item.price}, quantity: {item.quantity}\n")
            return item

    @classmethod
    def find(cls):
        while True:
            search = input("How do you want to search for a book by ID or title? ").lower().strip()
            if search == 'id':
                print("Search book by ID")
                attribute = input("What is the ID of the book you are looking for? ")
                list_of_ids = [i.ID for i in cls.inventory]
                match = list_of_ids.count(attribute)
                if match > 0:
                    book_location = list_of_ids.index(attribute)
                    return cls.inventory[book_location]
                else:
                    print("book not in inventory")
                    return None
            elif search == 'title':
                print("Search book by title")
                attribute = input("What is the title of the book you are looking for? ").lower().strip()
                list_of_titles = [i.title for i in cls.inventory]
                match = list_of_titles.count(attribute)
                if match > 0:
                    book_location = list_of_titles.index(attribute)
                    return cls.inventory[book_location]
                else:
                    print("book not in inventory")
                    return None
            else:
                print("Please type a valid option")

    @staticmethod
    def is_float(string):
        try:
            value = float(string)
            return value == round(value, 2)
        except ValueError:
            return False

    @staticmethod
    def price_set():
        while True:
            price = input("What is the book's new price? £")
            if Book.is_float(price):
                price = float(price)
                return price
            else:
                print("(Please type a valid price (max 2 decimal places))")

    @staticmethod
    def view_categories():
        available_categories = [book.category.lower() for book in Book.inventory]
        available_categories = tuple(available_categories)
        if len(available_categories) == 0:
            print('We do not have books in our system at the moment')
            return None
        else:
            print("These are the following categories available")
            [print(f"-{i.title()}") for i in available_categories]
            while True:
                requested_category = input('What type of books are you looking for: ').lower().strip()
                if requested_category in available_categories:
                    return requested_category
                elif requested_category == 'quit':
                    return None
                else:
                    print("We currently do not have books of that category: \n\
Either select one that it's in the list of categories available or type (quit) to go to main menu")


class Users:
    all_user_instances = []
    all_user_usernames = []

    def __init__(self, username: str, password, email=''):
        self.username = username
        self.password = password
        self.email = email
        Users.all_user_instances.append(self)
        Users.all_user_usernames.append(self.username)

    @classmethod
    def log_out(cls):
        return False

    @classmethod
    def log_in(cls):
        if len(cls.all_user_usernames) == 0:
            print("(There are currently no users registered. Please register)")
            return False
        in_username = input('What is your username: ')
        if in_username in cls.all_user_usernames:
            i = cls.all_user_usernames.index(in_username)
            user_instance = cls.all_user_instances[i]
            while True:
                in_password = input('What is your password: ')
                if in_password == user_instance.password:
                    return user_instance
                else:
                    end = input("Wrong password, press 'x' to go back to the main menu or anything else to try again ").lower().strip()
                    if end == 'x':
                        return False

        else:
            print('(The user does not exist, please register)')
            return False

    @staticmethod
    def see_inventory():
        if len(Book.inventory) == 0:
            print("\n(There are currently zero books in the inventory)")
        else:
            amount = len(Book.inventory)
            print(f"\n(There are currently {str(amount)} books in the inventory)")
            for i in Book.inventory:
                num = Book.inventory.index(i)
                print(f"{num}. Book: {i.title.title()}  |  Category: {i.category.title()}  |  ID: {i.ID}  |  Price: £{str(i.price)}  |  Quantity: {str(i.quantity)}")


class Customer(Users):
    all_customer_instances = []

    def __init__(self, username: str, password, email):
        super().__init__(username, password, email)
        Customer.all_customer_instances.append(self)

    @classmethod
    def customer_check(cls, user_instance):
        if user_instance in cls.all_customer_instances:
            return True
        else:
            return False

    # Shows suggestions of books under the category suggested
    @staticmethod
    def suggestion_category():
        requested_category = Book.view_categories()
        if requested_category is None:
            return
        list_of_recommendations = [recommendation for recommendation in Book.inventory if
                                   recommendation.category == requested_category]
        if len(list_of_recommendations) > 1:
            print(f"These are books we suggest which have the following category: {requested_category}.")
            for i in list_of_recommendations:
                print(f"-{i.title.title()} Stock amount: {i.quantity}")
        else:
            print(f"This is the only book that has the following category: {requested_category}.")
            for i in list_of_recommendations:
                print(f"-{i.title.title()} Stock amount: {i.quantity}")

    @staticmethod
    def view_books_by_category():
        requested_category = Book.view_categories()
        if requested_category is None:
            return
        books_available = [book for book in Book.inventory if book.category == requested_category and book.quantity > 0]
        if len(books_available) > 1:
            print(
                f"These are the following books with the category {requested_category.title()} that are available for purchase")
            for i in books_available:
                print(f"-{i.title.title()} Price: £{i.price} Stock amount: {i.quantity}")
        elif len(books_available) == 1:
            print(f"\nThis is the only book with the category {requested_category.title()} left that is available for purchase")
            for i in books_available:
                print(f"Title: {i.title.title()} Price: £{i.price} Stock amount: {i.quantity}")
        else:
            print(f"We do not have any books with {requested_category} available for purchase")

    @staticmethod
    def view_books():
        book = Book.find()
        if book is None:
            print("No book was found with those characteristics")
            return None
        else:
            print('Your book was found')
            print(f"{book.title.title()} Price: £{book.price} Quantity: {book.quantity}")
            return book

    @staticmethod
    def buy_book():
        book = Customer.view_books()
        if book is None:
            return
        while True:
            num = input(f"How many of {book.title.title()} do you want to buy? ")
            if num.isdigit():
                total_price = num * book.price
                while True:
                    answer = input(
                        f"Are you sure you want {str(num)} copy/s of {book.title.title()} for £{str(total_price)}?: (yes/no)").lower().strip()
                    if answer == 'yes':
                        book.sold_book(book, num)
                        break
                    elif answer == 'no':
                        print("Purchase was cas cancelled ")
                        return
                    else:
                        print("Please type yes or no")
            else:
                print("(Please type a valid number)")


class Admin(Users):
    all_admin_instances = []

    def __init__(self, username, password, email):
        super().__init__(username, password, email)
        Admin.all_admin_instances.append(self)

    @staticmethod
    def add_edit_book():
        if len(Book.inventory) == 0:
            Book.add_new_book()
            return
        else:
            print("Type the title or ID to add/edit book.")
            a, found_by, title_id = Book.check_for_book()
            if a is True:
                item = Book.get_book(found_by, title_id)
                item.edit_book()
                return
            elif a is False:
                print(f"Book doesn't already exists. Creating new book in inventory...")
                Book.add_new_book(found_by, title_id)
                return

    @staticmethod
    def sales():
        if len(Book.total_sales) == 0:
            print("\n(Currently there has not been any sale)")
        else:
            print("\nBOOKS SOLD:")
            [print(f"-{i.title()}: {str(j['qty_sold'])} copy/s") for i, j in zip(Book.total_sales.keys(), Book.total_sales.values())]

    @staticmethod
    def income():
        if len(Book.total_sales) == 0:
            print("\n(Currently there has not been any sale)")
        else:
            total_income = [i['total_income'] for i in Book.total_sales.values()]
            print(f"\nThe total amount of money made has been £{sum(total_income)}")

# I am so confused

# class User(Users):
#     user = []
#
#     def __init__(self, username: str, password, email, access: 'y'):
#         super().__init__(username, password, email)
