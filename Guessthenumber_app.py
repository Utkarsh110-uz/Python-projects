# Importing modules
from tkinter import *
import random

# Creating main window
window = Tk()

# Window related operations
window.title("Guess The Number Game")
window.config(bg="")
window.geometry("300x300")

# Creating label
output_label = Label(window, text="Output")
output_label.pack(pady=5)

# Creating input
a = Entry()
a.pack()

# Creating function
def check():
    n = random.randint(1, 100) 
    b = -1 
    guesses = 1
    while(b != n):
        b = int(a.get())
        if(b > n):
            output_label.config(text="Enter lower number")
            guesses += 1
        elif(b < n): 
            output_label.config(text="Enter higher number")
            guesses += 1
    output_label.config(text=f"You have guessesed the number {n} in {guesses} attempt")

# Creating buttons
check_button = Button(window, text="Check", command=check)
check_button.pack(pady=5)

exit_button = Button(window, text="Quit", command=window.destroy)
exit_button.pack()

window.mainloop()