# def greet():
#     def welcome():
#         print("Greeting")

#     return welcome


# func = greet()
# func()

import re


def isEmail(signup):
    def innerFunc(*args):
        print("Inside inner function")
        matched = re.search("[0-9a-z]{1,50}@[0-9a-z]{1,50}\.[a-z]{2,4}", args[1])
        if matched:
            print("Calling signup function")
            signup(args[0], args[1], args[2])
        else:
            print("Please enter a valid email address.")

        # If email is valid then call signup function
        # signup("dulal", "dulal@gmail.com", "123123")
        # else print some error message

    return innerFunc


@isEmail
def signup(name, email, password):
    print("Signup successfully")


signup("dulal", "dulal@gmail.com", "123123")
