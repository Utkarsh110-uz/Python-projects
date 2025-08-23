# Calculator:

number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))
operation = input("Enter operation of your type: ")

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