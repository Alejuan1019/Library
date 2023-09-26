from classes import *

security = '1234'


def register_user():
    username = input("Write a username: ")
    if username in Users.all_user_usernames:
        print("(This user already exists please Log in)")
        return False
    else:
        password = input("Write a password: ")
        email = input("What is your email: ")
        return username, password, email


def register_admin():
    a = register_user()
    if a is False:
        return False
    else:
        username = a[0]
        password = a[1]
        email = a[2]
        while True:
            keycode = input("Insert keycode to register as an admin (type 'quit' to register as a user): ")
            if keycode == security:
                print('\nThat was the correct keycode registering as an admin')
                user_instance = Admin(username, password, email)
                print("(Admin successfully registered)")
                return
            elif keycode == 'quit':
                print('Registering as user ... ')
                user_instance = Customer(username, password, email)
                print("(User successfully registered)")
                return
            else:
                print('Incorrect keycode')


def register():
    while True:
        choice = input("Do you want to register as user or admin: ").lower()
        if choice == 'admin':
            a = register_admin()
            if a is False:
                return False
            return True
        elif choice == 'user':
            a = register_user()
            if a is False:
                return False
            else:
                username = a[0]
                password = a[1]
                email = a[2]
                user_instance = Customer(username, password, email)
                print('(User successfully registered)')
                return True
        else:
            print('Please choose if you want to register as an admin or user')

