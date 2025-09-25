# Calculator:

number1 = float(input("Enter number 1: ")) # Here we are taking number from the user.
number2 = float(input("Enter number 2: ")) # Here we are taking number from the user.
operation = input("Enter operation of your type: ") # Here we are asking for the operation we are gonna perform on the numbers given.

# Below are written if-elif-else ladder which will perfom operation like an calculator.
if("+" in operation):
    print(f"The Addition of two numbers is: {number1 + number2}")
elif("-" in operation):
    print(f"The Subtraction of two numbers is: {number1 - number2}")
elif("*" in operation):
    print(f"The multiplication of two numbers is: {number1 * number2}")
elif("/" in operation):
    print(f"The divison of two numbers is: {number1 / number2}")
else:
    print("Please select the valid operator")