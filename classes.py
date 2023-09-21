import os
import copy
print(os.getcwd())


class Error(Exception):
    pass


class Book:
    inventory = []
    books_ID = []

    def __init__(self, title: str, category: str, ID: str, price: float, quantity=1, ):
        self.title = title
        self.category = category
        self.ID = ID
        self.price = price
        self.quantity = quantity
        Book.inventory.append(self)

    def sold_book(self, num: int):
        if num <= self.quantity and self.quantity > 0:
            total_price = num * self.price
            self.quantity = self.quantity - num
            print(f"You have purchased {str(num)} copy/s of {self.title} for {str(total_price)}")
        elif self.quantity == 0:
            Error(f"Sorry, we don't have any available copy for {self.title}")
        elif self.quantity > 1:
            Error(f"Sorry, {self.title}, has only {str(self.quantity)} copies available ")
        else:
            Error(f"Sorry, {self.title}, has only {str(self.quantity)} copy available ")

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
                    book = list_of_ids.index(attribute)
                    return cls.inventory[book]
                else:
                    print("book not in inventory")
                    return None
            elif search == 'title':
                print("Search book by title")
                attribute = input("What is the title of the book you are looking for? ")
                list_of_titles = [i.title for i in cls.inventory]
                match = list_of_titles.count(attribute)
                if match > 0:
                    book = list_of_titles.index(attribute)
                    return cls.inventory[book]
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
            price = input("What is the book's price")
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
                    break
                else:
                    print("That is not a valid option, please select an that it's in the list of categories available")
                    return None
            return requested_category


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
        return True

    @classmethod
    def log_in(cls):
        in_username = input('What is your username: ')
        if in_username in cls.all_user_usernames:
            i = cls.all_user_usernames.index(in_username)
            while True:
                in_password = input('What is your password: ')
                if cls.all_user_instances[i].password == in_password:
                    return True
                else:
                    end = input("Wrong password, press 'r' to register or anything else to continue ").lower()
                    if end == 'r':
                        return False

        else:
            print('The user does not exist, please register')
            return False

    @staticmethod
    def see_inventory():
        for i in Book.inventory:
            print(f"Title: {i.title}, qty: {i.quantity}")


class Customer(Users):
    all_customer_instances = []

    def __init__(self, username: str, password, email):
        super().__init__(username, password, email)
        Customer.all_customer_instances.append(self)

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
    def view_books_by_title():
        search = input("What book are you looking for: ").lower()
        books = [book for book in Book.inventory if book.title == search]
        if len(books) > 0:
            book = books[0]
            print('Your book was found')
            print(f"{book.title} Price: £{book.price} Quantity: {book.quantity}")
            return book
        else:
            print(f"No book was found with title: {search}")
            return None

    @staticmethod
    def buy_book():
        book = Customer.view_books_by_title()
        if book is None:
            return
        num = int(input("How many books do you want to buy"))
        total_price = num * book.price
        while True:
            answer = input(
                f"Are you sure you want to {str(num)} copy/s of {book.title} for £{str(total_price)}?: (yes/no)").lower()
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
        item = Book.find()
        if item is None:
            title = input("What is the tittle of the book? ").lower()
            category = input("What it's the book category ").lower()
            ID = input("What it's the book's ID? ")
            price = Book.price_set()
            quantity = int(input("How many books are you adding to the system? "))
            book = Book(title, category, ID, price, quantity)
            return
        else:
            print("The following book has been found\n")
            print(
                f"Title: {item.title}, Category: {item.category}, ID: {item.ID}, price: £{item.price}, quantity: {item.quantity}\n")
            while True:
                choice = input("What do you want to edit? ").lower()
                if choice == 'title':
                    print(f"\nUpdate {item.title}'s title")
                    new_title = input("\nWhat is the new title? ")
                    old_title = copy.deepcopy(item.title)
                    item.title = new_title
                    print(f"\n{old_title} has changed to {item.title}")
                    return
                elif choice == 'category':
                    print(f"\nUpdate {item.title}'s category")
                    new_category = input("\nWhat is the new category for this book? ")
                    old_category = copy.deepcopy(item.category)
                    item.category = new_category
                    print(f"\n{item.title}'s category has changed from {old_category} to {item.category}")
                    return
                elif choice == 'id':
                    print(f"\nUpdate {item.title}'s ID")
                    new_ID = input("\nWhat is the new ID ")
                    old_ID = copy.deepcopy(item.ID)
                    item.ID = new_ID
                    print(f"\n{item.title}'s ID has changed from {old_ID} to {item.ID}")
                    return
                elif choice == 'price':
                    print(f"Please type {item.title}'s new price) - ", end='')
                    new_price = Book.price_set()
                    old_price = copy.deepcopy(item.price)
                    item.price = new_price
                    print(f"\n{item.title}'s category has changed from £{str(old_price)} has changed to £{str(item.price)}")
                elif choice == 'quantity':
                    while True:
                        choice = input("\nDo you want to add more: ").lower()
                        if choice == 'yes':
                            while True:
                                add = input("\nHow many books do you want to add: ")
                                if add.isnumeric():
                                    new_qty = item.quantity + int(add)
                                    item.quantity = new_qty
                                    print(
                                        f"\n {add} book/s have been added and the new quantity is {str(item.quantity)}")
                                    return
                                else:
                                    print("(Please type a valid number)")
                        elif choice == 'no':
                            print(f"\nUpdate {item.title}'s quantity")
                            while True:
                                new_qty = input("\nHWhat is the new quantity for {item.title}: ")
                                if new_qty.isnumeric():
                                    item.quantity = new_qty
                                    print(f"\n {item.title}'s new quantity is {str(item.quantity)}")
                                    return
                                else:
                                    print("(Please type a valid number)")
                        else:
                            print("Type yes or no")
                else:
                    print("(please select a valid option: title, category, ID, price or quantity)")

    def sales(self):
        pass

    def income(self):
        pass

# I am so confused

# class User(Users):
#     user = []
#
#     def __init__(self, username: str, password, email, access: 'y'):
#         super().__init__(username, password, email)
