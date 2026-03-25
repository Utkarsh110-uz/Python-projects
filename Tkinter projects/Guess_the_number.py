# Importing modules
from tkinter import *
from tkinter import ttk
import random

# Creating main window
root = Tk()

# Main window related operations
root.title("Guess the number")
root.geometry("300x300")
root.config(bg="#6e6b79")

# Global variables
random_number = random.randint(1, 100)
guesses = 0

# Functions

# Game function that helps in playing game
def game():
    global guesses

    user_input = number_input.get()

    if not user_input.strip():
        display_label.config(text="Please enter number first")
        return
    
    number = int(user_input)
    guesses += 1

    if number > random_number:
        display_label.config(text="Enter Lower number please")
    elif number < random_number:
        display_label.config(text="Enter Higher number please")
    else:
        display_label.config(text=f"You guessed the number {random_number} in {guesses} attempts")

# Function that shows the random number
def show_number():
    display_label.config(text=random_number)

# CLearing function
def clear():
    number_input.delete(0, END)
    display_label.config(text="Your guessed number will be shown here")

# Button related styles
btn_style = ttk.Style()
btn_style.theme_use("default")
btn_style.configure("Custom.TButton", background="#7c3aed", foreground="#ffffff", font=("Helvetica", 14, "bold"), focuscolor="none")
btn_style.map("Custom.TButton", background=[("active", "#7c3aed")], foreground=[("active", "#ffffff")])


# Top level heading label
top_label = Label(root, text="Guess the number game", bg="#6e6b79", fg="#ffffff", font=("Helvetica", 16, "bold"))
top_label.pack(pady=5)

# User input entry
number_input = Entry(width=5, bg="#2d2650", fg="#ffffff", insertbackground="white", font=("Helvetica", 13))
number_input.pack(pady=5)

# Result label
display_label = Label(root, text="Your guessed number will be showed here", bg="#6e6b79", fg="#000000", font=("Helvetica", 14))
display_label.pack(pady=5)

# Buttons

# Show number button
show_number_btn = ttk.Button(root, text="Show number", width=14, command=show_number, style="Custom.TButton")
show_number_btn.pack(pady=5)

# Check button
check_btn = ttk.Button(root, text="Check", width=14, command=game, style="Custom.TButton")
check_btn.pack(pady=5)

# Clear button
clear_btn = ttk.Button(root, text="Clear", command=clear, width=14, style="Custom.TButton")
clear_btn.pack(pady=5)

# Quit button
quit_btn = ttk.Button(root, text="Quit", command=root.destroy, width=14, style="Custom.TButton")
quit_btn.pack(pady=5)

# Closing the main window
root.mainloop()