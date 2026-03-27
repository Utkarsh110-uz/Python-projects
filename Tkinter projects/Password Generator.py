# Importing modules
from tkinter import *
from tkinter import ttk
import random

# Creating main window
root = Tk()

# Main window related operations
root.title("Random Password Generator")
root.geometry("400x200")
root.config(bg="#0d1117")

# Defined functions

# Password generator password
def password_generator(length=12):
    char = "abcdefghijklmnopqrstuvwxyz1234567890-+=!@#$%^&*()~`<,>.?/';:{}[]\\|"
    global new_password
    new_password = "".join(random.choice(char) for _ in range(length))
    display_label.config(text=new_password)

# Claer function
def clear():
    display_label.config(text="Generated password will be shown here")

# Button styles
btn_styles = ttk.Style()
btn_styles.theme_use("default")
btn_styles.configure("Custom.TButton", background="#238636", foreground="#ffffff", font=("Courier New", 12, "bold"), focuscolor="none")
btn_styles.map("Custom.TButton", background=[("active", "#238636")], foreground=[("active", "#ffffff")])

# Display Label
display_label = Label(root, text="Generated password will be shown here", bg="#0d1117", fg="#3fb950", font=("Courier New", 13, "bold"))
display_label.pack(pady=5)

# Buttons

# Generate button
generate_button = ttk.Button(root, text="Generate", command=password_generator, style="Custom.TButton")
generate_button.pack(pady=5)

# Clear button
claer_button = ttk.Button(root, text="Clear", command=clear, style="Custom.TButton")
claer_button.pack(pady=5)

# Quit button
quit_button = ttk.Button(root, text="Quit", command=root.destroy, style="Custom.TButton")
quit_button.pack(pady=5)

# Closing the main window
root.mainloop()