from tkinter import *
from tkinter import ttk
import random

root = Tk()

root.title("Rolling Dice")
root.geometry("300x200")

def roll():
    display_label.config(text=f"{random.randint(1, 6)}")

display_label = Label(root, text="Number is")
display_label.pack(pady=5)

roll_btn = ttk.Button(root, text="Roll The Dice", command=roll)
roll_btn.pack(pady=5)

quit_btn = ttk.Button(root, text="Quit", command=root.destroy, width=9)
quit_btn.pack(pady=5)

root.mainloop()