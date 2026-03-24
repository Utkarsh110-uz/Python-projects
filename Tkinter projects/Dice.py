# Importing moudles
from tkinter import *
from tkinter import ttk
import random

# Creating main window
root = Tk()

# Main widnow related operations
root.title("Rolling Dice")
root.geometry("300x200")
root.config(bg="#88798E")

# Defined functions

# Rolling function this shows the number of the screen
def roll():
    display_label.config(text=f"{random.randint(1, 6)}")

# Button styles
btn_style = ttk.Style()
btn_style.theme_use("default")
btn_style.configure("Dice.TButton", background="#c9567b", foreground="#ffffff", font=("Comic Sans MS", 12, "bold"), focuscolor="none")
btn_style.map("Dice.TButton", background=[("active", "#c9567b")], foreground=[("active", "#ffffff")])

# Display label
display_label = Label(root, text="Number is", bg="#88798E", fg="#ff9ecd", font=("Comic Sans MS", 16, "bold"))
display_label.pack(pady=5)

# Buttons

# Rolling button
roll_btn = ttk.Button(root, text="Roll The Dice", command=roll , style="Dice.TButton")
roll_btn.pack(pady=5)

# Quit button
quit_btn = ttk.Button(root, text="Quit", command=root.destroy, width=9 , style="Dice.TButton")
quit_btn.pack(pady=5)

root.mainloop() # Closing main window