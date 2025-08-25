from tkinter import *
import tkinter as tk
import time

root = Tk()
root.title("Digital clock")
root.config(bg="#FFBF00")

def update_time():
    current_time = time.strftime("%H:%M:%S %p")
    current_date = time.strftime("%A, %d %B %Y")

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    root.after(1000, update_time)

time_label = Label(root,bg="#FFBF00", fg="#000000", font=("MS Gothic", 60))
time_label.pack(pady=20)

date_label = Label(root,bg="#FFBF00", fg="#000000", font=("MS Gothic", 30))
date_label.pack(pady=20)

button = Button(root, text="Quit", width=25, command=root.quit, bg="#FFECD1", fg="#FF0000", font=("Arial", 15))
button.pack()

update_time()

root.mainloop()