import random
from tkinter import *
import tkinter as tk

root = Tk()
root.title("Snake_water_gun Game")
root.config(bg="#E3ACA1")

heading = Label(root, text= "Welcome to the game", font=("Arial Bold", 20),background="#E3ACA1", foreground="#2B024C")
heading.pack(pady=10)

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text="Enter move", font=("Arial", 15)).grid(row=0, padx=10, pady=10)
e1 = Entry(frame)
e1.grid(row=0, column=1, padx=10, pady=10)

def game():
    youstr = e1.get()
    computer = random.choice([1,2,3])
    dict = {"snake": 1, "water": 2, "gun": 3}
    rev_dict = {1: "Snake", 2: "Water", 3: "Gun"}
    you = dict[youstr]
    print(f"You chose: {rev_dict[you]}\nComputer chose: {rev_dict[computer]}")

    if((computer - you) == 1 or (computer - you) == -2):
        # print("You win!")
        result_label.config(text="You win")
    else:
        # print("You lose!")
        result_label.config(text="You lose")
# game()
result_label = Label(root, text="Result", font=("Arial", 15), bg="#E3ACA1", fg="red")
result_label.pack(pady=5)

game_button = Button(root, text="Click to see", command=game, bg="#D5EDC2", font=("Arial Bold", 12))
game_button.pack(pady=10)

button = tk.Button(root, text="Exit Program", width=25, command=root.destroy, background="#EB6565", font=("Arial Bold", 12))
button.pack(pady=10)

root.mainloop()