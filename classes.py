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
            choice = input("What do you want to edit? Type which one you want to edit (Title/Category/ID/Price/Quantity) or type (quit) to exit: ").lower()
            if choice == 'title':
                print(f"\nUpdate {self.title.title()}'s title")
                new_title = input("\nWhat is the new title?")
                old_title = copy.deepcopy(self.title)
                self.title = new_title
                print(f"\n{old_title} has changed to {self.title.title()}")
            elif choice == 'category':
                print(f"\n{self.title.title()}'s current category is {self.category.title()}")
                new_category = input("\nWhat is the new category for this book? ")
                old_category = copy.deepcopy(self.category)
                self.category = new_category
                print(f"\n{self.title.title()}'s category has changed from {old_category} to {self.category.title()}")
            elif choice == 'id':
                print(f"\n{self.title.title()}'s current ID is {self.ID}")
                new_ID = input("\nWhat is the new ID for this book? ")
                old_ID = copy.deepcopy(self.ID)
                self.ID = new_ID
                print(f"\n{self.title.title()}'s ID has changed from {old_ID} to {self.ID}")
            elif choice == 'price':
                print(f"{self.title.title()}'s current price is £{str(self.price)}")
                new_price = Book.price_set()
                old_price = copy.deepcopy(self.price)
                self.price = new_price
                print(f"\n{self.title.title()}'s price has changed from £{str(old_price)} has changed to £{str(self.price)}")
            elif choice == 'quit':
                return
            elif choice == 'quantity':
                while True:
                    print(f"{self.title.title()}'s current quantity in stock is £{str(self.quantity)}")
                    choice = input("\nDo you want to add more: ").lower()
                    if choice == 'yes':
                        while True:
                            add = input("\nHow many books do you want to add: ")
                            if add.isnumeric():
                                new_qty = int(self.quantity) + int(add)
                                self.quantity = new_qty
                                print(
                                    f"\n {add} book/s have been added and the new quantity in stock for {self.title.title()} is {str(self.quantity)}")
                                return
                            else:
                                print("(Please type a valid number)")
                    elif choice == 'no':
                        print(f"\nUpdating {self.title.title()}'s quantity")
                        while True:
                            new_qty = input(f"\nHWhat is the new quantity for {self.title.title()}: ")
                            if new_qty.isnumeric():
                                self.quantity = new_qty
                                print(f"\n {self.title.title()}'s new quantity is {str(self.quantity)}")
                                return
                            else:
                                print("(Please type a valid number)")
                    else:
                        print("Type yes or no")
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
    def add_new_book(cls, title, ID):
        category = input("What it's the book category ").lower()
        price = cls.price_set()
        quantity = int(input("How many books are you adding to the system? "))
        book_instance = Book(title, category, ID, price, quantity)
        print("\nThe following has been added to the inventory")
        print(f"(Book: {title} Category: {category} ID: {ID} Price: £{str(price)} Quantity: {str(quantity)}")
        return

    @classmethod
    def check_for_book(cls, title, ID,):
        list_of_ids = [i.ID for i in cls.inventory]
        match = list_of_ids.count(ID)
        if match > 0:
            return True, 'ID'
        else:
            list_of_titles = [i.title for i in cls.inventory]
            match = list_of_titles.count(title)
            if match > 0:
                return True, 'title'
            else:
                return False, 'N/A'

    @classmethod
    def get_book(cls, tittle, ID, found_by):
        if found_by == 'ID':
            list_of_ids = [i.ID for i in cls.inventory]
            book_location = list_of_ids.index(ID)
            item = cls.inventory[book_location]
            print("The following book has been found\n")
            print(
                f"Title: {item.title}, Category: {item.category}, ID: {item.ID}, price: £{item.price}, quantity: {item.quantity}\n")
            return item
        elif found_by == 'title':
            list_of_titles = [i.title for i in cls.inventory]
            book_location = list_of_titles.index(tittle)
            item = cls.inventory[book_location]
            print("The following book has been found\n")
            print(
                f"Title: {item.title}, Category: {item.category}, ID: {item.ID}, price: £{item.price}, quantity: {item.quantity}\n")
            return item
        else:
            'NA error'
    @classmethod
    def find(cls):
        while True:
            search = input("How do you want to search for a book by ID or title? ").lower()
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
                attribute = input("What is the title of the book you are looking for? ").lower()
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
            price = input("What is the book's new price")
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
                requested_category = input('what type of books are you looking for: ').lower()
                if requested_category in available_categories:
                    return requested_category
                else:
                    print("That is not a valid option, please select an that it's in the list of categories available")
                    return None


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
        in_username = input('What is your username: ')
        if in_username in cls.all_user_usernames:
            i = cls.all_user_usernames.index(in_username)
            user_instance = cls.all_user_instances[i]
            while True:
                in_password = input('What is your password: ')
                if in_password == user_instance.password:
                    return user_instance
                else:
                    end = input("Wrong password, press 'x' to go back to the main menu or anything else to try again ").lower()
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
            for i in Book.inventory:
                print(f"Title: {i.title}, qty: {i.quantity}")


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
                f"These are the following books with the category {requested_category} that are available for purchase")
            for i in books_available:
                print(f"-{i.title.title()} Price: £{i.price} Stock amount: {i.quantity}")
        elif len(books_available) == 1:
            print(f"This is the only book with the category {requested_category} left that is available for purchase")
            for i in books_available:
                print(f"-{i.title.title()} Price: £{i.price} Stock amount: {i.quantity}")
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
        num = int(input(f"How many of {book.title.title()} do you want to buy"))
        total_price = num * book.price
        while True:
            answer = input(
                f"Are you sure you want {str(num)} copy/s of {book.title.title()} for £{str(total_price)}?: (yes/no)").lower()
            if answer == 'yes':
                book.sold_book(book, num)
                break
            elif answer == 'no':
                print("Purchase was cas cancelled ")
                return
            else:
                print("Please type yes or no")


class Admin(Users):
    all_admin_instances = []

    def __init__(self, username, password, email):
        super().__init__(username, password, email)
        Admin.all_admin_instances.append(self)

    @staticmethod
    def edit_book():
        choice = input("To add a new book press (1). To edit the characteristics of an existing book\n")
        if len(Book.inventory) == 0 or choice == 1:
            title = input("What is the tittle of the new book? ").lower()
            ID = input("What it's the book's ID? ")
            a, found_by = Book.check_for_book(title, ID)
            if a is True:
                print(f"Book already exists")
                choice = input("To edit it press (1) to exit press (2)")
                if choice == '1':
                    item = Book.get_book(title, ID, found_by)
                    item.edit_book()
                    return
                if choice == '2':
                    return
            else:
                Book.add_new_book(title, ID)
                return

        elif choice == '2':
            title = input("What is the tittle of the new book? ").lower()
            ID = input("What it's the book's ID? ")
            a, found_by = Book.check_for_book(title, ID)
            if a is False:
                print(f"Book doesn't already exists")
                choice = input("To add it press (1) to exit press (2)")
                if choice == '1':
                    Book.add_new_book(title, ID)
                    return
                if choice == '2':
                    return
            else:
                item = Book.get_book(title, ID, found_by)
                item.edit_book()
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
