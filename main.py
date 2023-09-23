from functions import *


def main():
    print("\n\nWELCOME TO JUAN'S LIBRARY")
    while True:
        choice = input("\nPress 1 to register, 2 to log in or 3 to quit: ")
        if choice == '1':
            a = register()
            if a is False:
                pass
            else:
                pass
        elif choice == '2':
            if log_in() is False:
                pass
            else:
                user_instance = log_in()
                break
        elif choice == '3':
            print('here i need to add stuff to quit and save the program')
        else:
            print("please type 1, 2, 3")
    # User
    if Customer.customer_check(user_instance):
        while True:
            print("\n Welcome to the customer portal you have the following options\n")
            print("\n-View books of a certain category (press 1)")
            print("\n-Look for a book by its title/ID (press 2)")
            print("\n-Let us give you a book suggestion based on the category of your choice (press 3)")
            print("\n-Buy a book (press 4)")
            print("\n-Log out (press 5)")
            choice = input('Answer: ')
            if choice == '1':
                Customer.view_books_by_category()
            elif choice == '2':
                Customer.view_books()
            elif choice == '3':
                Customer.suggestion_category()
            elif choice == '4':
                Customer.buy_book()
            elif choice == '5':
                pass
            else:
                print("(Please type a valid option)")
    # Admin
    elif not Customer.customer_check(user_instance):
        while True:
            print("\n Welcome to the Admin portal you have the following options\n")
            print("\n-View book inventory (press 1)")
            print("\n-Add/ edit existing book (press 2)")
            print("\n-See sales (press 3)")
            print("\n-See total income (press 4)")
            print("\n-Log out (press 5)")
            choice = input('Answer: ')
            if choice == '1':
                Users.see_inventory()
            elif choice == '2':
                Admin.edit_book()
            elif choice == '3':
                Admin.sales()
            elif choice == '4':
                Admin.income()
            elif choice == '5':
                pass
            else:
                print("(Please type a valid option)")

main()
