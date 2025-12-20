# Importing modules
from tkinter import *
import time

# Creating main window
window = Tk()

# Window related operations
window.title("Digital clock")
window.config(bg="lightcyan")
window.geometry("500x200")

# Creating function
def update_time():
    current_time = time.strftime("%H:%M:%S %p")  
    current_date = time.strftime("%A, %d %B %Y") 
    time_label.config(text=current_time) 
    date_label.config(text=current_date)

    window.after(1000, update_time)


# Creating label
time_label = Label(window,bg="lightcyan", fg="#000000", font=("MS Gothic", 30)) 
time_label.pack(pady=20)

date_label = Label(window,bg="lightcyan", fg="#000000", font=("MS Gothic", 30))
date_label.pack(pady=20)

# Creating button
exit_button = Button(window, text="Quit", command=window.destroy)
exit_button.pack()

update_time()

window.mainloop()