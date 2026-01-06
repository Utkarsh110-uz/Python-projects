# Importing modules
import random
from tkinter import *

# Creating main window
window = Tk()

# Window related operations
window.geometry("500x200")
window.title("Nuke the system")
window.config(bg="#E8D2CF")

# Making useful variables
number = random.randint(1, 100)

# Creating input
ask_input = Entry()
ask_input.pack()

# Creating functions
def check_result():
    value = int(ask_input.get())
    if value == number:
        output_label = Label(window, text="Yes this is the correct number", font=("Geeza Pro", 20, "bold"), bg="#E8D2CF", fg="Black")
        output_label.pack()
        with open("Gift.txt", "w") as f:
            f.write("Congrats you won")

def delete_input():
    ask_input.delete(0, END)

def show_number():
    number_label = Label(window, text=number, font=("Geeza Pro", 20, "bold"), bg="#E8D2CF", fg="Black")
    number_label.pack()

# Creating buttons
check_button = Button(window, text="Check", command=check_result)
check_button.pack(pady=5)

show_num_button = Button(window, text="Show", command=show_number)
show_num_button.pack(pady=5)

exit_button = Button(window, text="Quit", command=window.destroy)
exit_button.pack()

window.mainloop()