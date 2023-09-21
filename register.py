from classes import *

options = ['admin', 'user']
security = '1234'
users = {}
username = ''
password = ''
email = ''
access = ''


def register_user():
    global username, password, email, access
    username = input("Write an username: ")
    password = input("Write a password: ")
    email = input("What is your email: ")


def register_admin():
    global access
    register_user()
    while True:
        keycode = input("Insert keycode to register as an admin(type 'quit' to register as a user")
        if keycode == security:
            print('That was the correct keycode')
            break
        if keycode == 'quit':
            print('Registering as user ...')
            break
        else:
            print('Incorrect keycode')

    return username, password, email


def register():
    global username
    choice = input("Do you want to register as an user or admin ").lower()
    while choice not in options:
        print('Please choose if you want to register as an admin or user')
    if choice == 'admin':
        register_admin()
        user_instance = Admin(username, password, email)
    elif choice == 'user':
        register_user()
        user_instance = Customer(username, password, email)
    with open('users.cvs', 'a') as f:
        f.write(f"{username},{password},{email}")
