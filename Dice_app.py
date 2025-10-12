from tkinter import *
import tkinter as tk
import random

root = Tk()
root.title("Roll The Dice")
root.config(bg="white")

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text="Enter yes to roll dice", foreground="white", font=("Arial", 15)).grid(row=0, padx=10, pady=10)
e1 = Entry(frame)
e1.grid(row=0, column=1, padx=10, pady=10)

result_label = Label(root, text="Number is", font=("Arial", 15), bg="#D2C6F5")
result_label.pack(pady=5)

def dice_roll():
    user = e1.get()
    if("yes" in user):
        dice = random.randint(1, 6)
        result_label.config(text=f"{dice}")
    else:
        result_label.config(text="Please enter 'yes' or 'no'")

Dice_roll_button = Button(root, text="Roll the dice", command=dice_roll, bg="#D5EDC2", font=("Arial Bold", 12))
Dice_roll_button.pack(pady=10)

button = tk.Button(root, text="Exit", width=10, command=root.destroy, background="#EB6565", font=("Arial Bold", 12))
button.pack(pady=10)

root.mainloop()