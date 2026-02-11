from tkinter import *
from os import *

window = Tk()

window.title("Sample GUI")
window.geometry("200x200")
window.config(bg="lightblue")

def download_content():
    content = user_input.get()
    system(content)
    message_label = Label(window, text="Task Completed")
    message_label.pack(pady=5)

def clear_content():
    user_input.delete(0, END)

user_input = Entry()
user_input.pack(pady=5)

download_button = Button(window, text="Download", command=download_content)
download_button.pack(pady=5)

clear_button = Button(window, text="Clear", command=clear_content)
clear_button.pack(pady=5)

quit_button = Button(window, text="Quit", command=window.quit)
quit_button.pack(pady=5)

window.mainloop()

'''
Functions we can add in this are:

1. Backup the user inputs.

2. Show the progress.

3. Add message when download is finished or if any error occured.
'''