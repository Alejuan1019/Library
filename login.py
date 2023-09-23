from classes import *


def log_in():
    user_instance = Users.log_in()
    if user_instance is False:
        return False
    else:
        if Customer.customer_check(user_instance):
            print(f"Welcome back user {user_instance.username}")
            return user_instance
        else:
            print(f"Welcome back admin {user_instance.username}")
            return user_instance

