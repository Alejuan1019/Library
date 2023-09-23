from classes import *


def log_in():
    user_instance = Users.log_in()
    if user_instance is False:
        return False
    else:
        return user_instance

