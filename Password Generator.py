import random
# Here we wrapped the whole function of password generator in a function.
def password_gen(length=12):
    char = '''abcdefjhigklmnopqrstuvwxyzABCDEFGHIZKLMNOPQRSTUVWXYZ1234567890./*-+!@#$%^&()-_=~`{}[]:;',.<>?"''' # Here we used every possible chracters to help us generate a random password we used random moudle for that

    # Here first in join we picked one character from the above given string and using for loops we will repeat this process number of times and then we are gonna return this to our funtion
    password = "".join(random.choice(char) for _ in range(length))
    return password
n = int(input("Enter a number to get a password that long: ")) # Here we are asking the user that how long password he/she wants
print(f"Generated password is: {password_gen(n)}") # Here we are printing the result.