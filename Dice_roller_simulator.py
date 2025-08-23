# Dice roller game:
import random

while True:
    user = input("Enter 'yes' to roll a dice or 'no' ro quit: ")
    if("yes" == user):
        dice = random.randint(1, 6)
        print(f"The number is: {dice}")
    elif("no" == user):
        print("The proram ended")
        break
    else:
        print("Please enter 'yes' or 'no'")