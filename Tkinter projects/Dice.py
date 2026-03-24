from tkinter import *
from tkinter import ttk
import random

root = Tk()

root.title("Rolling Dice")
root.geometry("300x200")
root.config(bg="#88798E")

def roll():
    display_label.config(text=f"{random.randint(1, 6)}")

btn_style = ttk.Style()
btn_style.theme_use("default")
btn_style.configure("Dice.TButton", background="#c9567b", foreground="#ffffff", font=("Comic Sans MS", 12, "bold"), focuscolor="none")
btn_style.map("Dice.TButton", background=[("active", "#c9567b")], foreground=[("active", "#ffffff")])

display_label = Label(root, text="Number is", bg="#88798E", fg="#ff9ecd", font=("Comic Sans MS", 16, "bold"))
display_label.pack(pady=5)

roll_btn = ttk.Button(root, text="Roll The Dice", command=roll , style="Dice.TButton")
roll_btn.pack(pady=5)

quit_btn = ttk.Button(root, text="Quit", command=root.destroy, width=9 , style="Dice.TButton")
quit_btn.pack(pady=5)

root.mainloop()