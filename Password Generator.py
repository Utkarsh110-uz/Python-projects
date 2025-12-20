import random

def password_gen(length=12):
    char = '''abcdefjhigklmnopqrstuvwxyzABCDEFGHIZKLMNOPQRSTUVWXYZ1234567890./*-+!@#$%^&()-_=~`{}[]:;',.<>?"'''  
    password = "".join(random.choice(char) for _ in range(length))
    return password

n = int(input("Enter a number to get a password that long: ")) 
print(f"Generated password is: {password_gen(n)}")