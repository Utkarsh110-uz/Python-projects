from tkinter import *
import tkinter as tk
import time

root = Tk() # Creating the main window
root.title("Digital clock")
root.config(bg="#FFBF00")

def update_time():
    current_time = time.strftime("%H:%M:%S %p") # Here we are taking current time 
    current_date = time.strftime("%A, %d %B %Y") # Here we are taking current date

    time_label.config(text=current_time) # Here we are updating the time
    date_label.config(text=current_date) # Here we are updating the date

    root.after(1000, update_time) # Here we are calling the function again after 1000ms (1 second)keeps the clock ticking continuously.  

time_label = Label(root,bg="#FFBF00", fg="#000000", font=("MS Gothic", 60)) # Here we are shwoing the current time 
time_label.pack(pady=20)

date_label = Label(root,bg="#FFBF00", fg="#000000", font=("MS Gothic", 30)) # Here we are shwoing the current date 
date_label.pack(pady=20)

button = Button(root, text="Quit", width=25, command=root.quit, bg="#FFECD1", fg="#FF0000", font=("Arial", 15))
button.pack() # Here we have made one quit button to leave the clock application

update_time() # When this function is called the time is updated automatically its is called only one time

root.mainloop() # Closing the main window