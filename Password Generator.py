# Importing Modules
from tkinter import *
import random

# Initializng main window
root = Tk()

# Window related operations
root.title("Password Generator") # Setting the title of the window
root.geometry("500x200") # Setting the geometry of the window

# Below defined functions creates a random password of 12 characterstics
def password_gen(length=12):
    char = '''abcdefjhigklmnopqrstuvwxyzABCDEFGHIZKLMNOPQRSTUVWXYZ1234567890./*-+!@#$%^&()-_=~`{}[]:;',.<>?"'''  
    password = "".join(random.choice(char) for _ in range(length))
    show_password.config(text=password)

# Passoword showing Lable
show_password = Label(root, text="Your Generated password will be show here", font=("Galvji", 16, "bold"))
show_password.pack(pady=5)

# Password generator Button
generate_password = Button(root, text="Generate password", command=password_gen, width=12)
generate_password.pack(pady=5)

# Quit button
quit_button = Button(root, text="Quit", command=root.quit, width=12)
quit_button.pack(pady=5)

root.mainloop() # Closing the loop of the window