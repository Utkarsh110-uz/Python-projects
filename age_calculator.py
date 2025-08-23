# Age Calculator
import datetime

def age():
    current_year = datetime.datetime.now().year

    operation_ask = input("Enter 'age' to calculate age or 'year' to calculate year: ")
    if("age" in operation_ask):
        ask_year = int(input("Enter your birth year: "))
        ask = input("Has your birthday came: ")
        if("yes" in ask):
            print(f"Your current age is: {current_year - ask_year}")
        elif("no" in ask):
            print(f"Your age till now is: {current_year - ask_year - 1}")
        else:
            print("Please enter 'yes' or 'no'")

    elif("year" in operation_ask):
        ask_age = int(input("Enter your age here: "))
        ask = input("Has your birthday came: ")
        if("yes" in ask):
            print(f"Your birth year is: {current_year - ask_age}")
        elif("no" in ask):
            print(f"Your birth year is: {current_year - ask_age - 1}")
        else:
            print("Please enter 'yes' or 'no'")
age()