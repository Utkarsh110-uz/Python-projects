from tkinter import *
import tkinter as tk
import time

root = Tk()
root.title("Digital clock")
root.config(bg="#FFBF00")

def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %d %B %Y %p")

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    root.after(1000, update_time)

time_label = Label(root, fg="#FAA291", font=("Arial", 60))
time_label.pack(pady=20)

date_label = Label(root, fg="#A0A677", font=("Arial", 30))
date_label.pack(pady=20)

button = Button(root, text="Quit", width=25, command=root.quit, bg="#45A8D9", fg="#F4FAE8")
button.pack()

update_time()

root.mainloop()