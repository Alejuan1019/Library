from functions import *


def main():
    print("\n\nWELCOME TO JUAN'S LIBRARY")
    while True:
        choice = input("\nPress 1 to register, 2 to log in or 3 to quit: ")
        if choice == '1':
            a = register()
            # If user is already register then pass
            if a is False:
                pass
            # User was successfully registered
            else:
                pass
        elif choice == '2':
            user_instance = log_in()
            # If user is already register then pass
            if user_instance is False:
                pass
            # User was successfully registered as admin or customer
            else:
                check = Customer.customer_check(user_instance)
                # User
                if check is True:
                    print(f"(Welcome back user {user_instance.username}! ...)")
                    while True:
                        print("\nWelcome to the customer portal you have the following options\n")
                        print("-View inventory (press 1)")
                        print("-View books of a certain category (press 2)")
                        print("-Look for a book by its title/ID (press 3)")
                        print("-Let us give you a book suggestion based on the category of your choice (press 4)")
                        print("-Buy a book (press 5)")
                        print("-Log out (press 6)")
                        choice = input('\nAnswer: ').strip()
                        if choice == '1':
                            Users.see_inventory()
                        elif choice == '2':
                            Customer.view_books_by_category()
                        elif choice == '3':
                            Customer.view_books()
                        elif choice == '4':
                            Customer.suggestion_category()
                        elif choice == '5':
                            Customer.buy_book()
                        elif choice == '6':
                            print("logging out")
                            break
                        else:
                            print("(Please type a valid option)")
                # Admin
                elif check is False:
                    print(f"(Welcome back admin {user_instance.username}!...)")
                    while True:
                        print("\nWelcome to the Admin portal you have the following options\n")
                        print("-View book inventory (press 1)")
                        print("-Add/ edit existing book (press 2)")
                        print("-See sales (press 3)")
                        print("-See total income (press 4)")
                        print("-Log out (press 5)")
                        choice = input('\nAnswer: ').strip()
                        if choice == '1':
                            Users.see_inventory()
                        elif choice == '2':
                            Admin.add_edit_book()
                        elif choice == '3':
                            Admin.sales()
                        elif choice == '4':
                            Admin.income()
                        elif choice == '5':
                            print("logging out")
                            break
                        else:
                            print("(Please type a valid option)")
        elif choice == '3':
            print('here i need to add stuff to quit and save the program')
        else:
            print("please type 1, 2, 3")


main()
