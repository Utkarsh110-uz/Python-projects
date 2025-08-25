import random
def password_gen(length=12):
    char = '''abcdefjhigklmnopqrstuvwxyz1234567890./*-+!@#$%^&()-_=~`{}[]:;',.<>?"'''

    password = "".join(random.choice(char) for _ in range(length))
    return password

print(f"Generated password is: {password_gen(500)}")