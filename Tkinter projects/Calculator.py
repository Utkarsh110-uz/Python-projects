# Importing modules
from tkinter import *
from tkinter import ttk

# Creating main window
root = Tk()

# Main window related operations
root.title("Calculator")
root.geometry("500x400")
root.configure(bg="#6E4E79")

# Functions for buttons

# Delete button function
def clear_content():
    input1.delete(0, END)
    input2.delete(0, END)
    display_label.config(text="Result will be show here")

# Add button function
def add():
    num1 = int(input1.get())
    num2 = int(input2.get())
    display_label.config(text=f"Your answers is: {num1 + num2}")

# Subtract button function
def sub():
    num1 = int(input1.get())
    num2 = int(input2.get())
    display_label.config(text=f"Your answers is: {num1 - num2}")

# Multiply button function
def mul():
    num1 = int(input1.get())
    num2 = int(input2.get())
    display_label.config(text=f"Your answers is: {num1 * num2}")

# Divide button function
def div():
    num1 = int(input1.get())
    num2 = int(input2.get())
    display_label.config(text=f"Your answers is: {num1 / num2}")

# Button styling information
btn_style = ttk.Style()
btn_style.theme_use("default")
btn_style.configure("Custom.TButton", background="#c9567b", foreground="#ffffff", focuscolor="none", font=("Comic Sans MS", 11, "bold"))
btn_style.map("Custom.TButton", background=[("active", "#c9567b")], foreground=[("active", "#ffffff")])

# First input field
input1 = Entry(width=9, bg="#3d2445", fg="#ffffff", insertbackground="white", font=("Comic Sans MS", 14))
input1.pack(pady=5)

# Second input field
input2 = Entry(width=9, bg="#3d2445", fg="#ffffff", insertbackground="white", font=("Comic Sans MS", 14))
input2.pack(pady=5)

# Display label
display_label = Label(root, text="Result will be shown here", bg="#6E4E79", fg="#ff9ecd", font=("Comic Sans MS", 13))
display_label.pack(pady=5)

# Buttons

# Add button
add_btn = ttk.Button(root, text="Add", command=add, style="Custom.TButton")
add_btn.pack(pady=5)

# Subtract button
sub_btn = ttk.Button(root, text="Sub", command=sub, style="Custom.TButton")
sub_btn.pack(pady=5)

# Multiply button
mul_btn = ttk.Button(root, text="Multiply", command=mul, style="Custom.TButton")
mul_btn.pack(pady=5)

# Divide button
div_btn = ttk.Button(root, text="Division", command=div, style="Custom.TButton")
div_btn.pack(pady=5)

# Delete button
delete_btn = ttk.Button(root, text="Clear", command=clear_content, style="Custom.TButton")
delete_btn.pack(pady=5)

# Quit button
quit_btn = ttk.Button(root, text="Quit", command=root.destroy, style="Custom.TButton")
quit_btn.pack(pady=5)

root.mainloop() # Closing the main window