# Importing modules
from tkinter import *
import random

# Initializing main window
window = Tk()

# Window related operations
window.title("Roll The Dice")
window.config(bg="lightcoral")
window.geometry("200x150")

# Initializing functions
def dice_roll():
    output_label.config(text=f"{random.randint(1, 6)}")

# Initializing label
output_label = Label(window, text="Number is", font=("Gill Sans", 15), bg="lightcoral")
output_label.pack(pady=5)

# Initializing buttons
roll_dice = Button(window, text="Roll Dice", command=dice_roll)
roll_dice.pack(pady=5)

exit_button = Button(window, text="Quit", command=window.destroy)
exit_button.pack()

window.mainloop()