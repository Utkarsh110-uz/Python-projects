# Snake Water Gun Game:

import random

computer = random.choice([1, 2, 3]) # Here computer chose random numbers from 123

youstr = input("Enter your move: ") # Here user will chose snake(s), water(w), gun(g)
dict = {"s": 1, "w": 2, "g": 3} # Here we crated a dict and given them the value to convert it for computer
revdict = {1: "Snake", 2: "Water", 3: "Gun"} # Here we made a reverse dict so that computer can understand user moves
you = dict[youstr] # Here we are collecting value in the form of number 123

print(f"You chose: {revdict[you]}\nComputer chose: {revdict[computer]}")
# Here below we used if-elif-else condition to instruct our code when and what to do on the basis of user moves/input
if(computer == you):
    print("It's a draw")
else:
    if(computer == 1 and you == 2): 
        print("You lose")
    elif(computer == 1 and you == 3): 
        print("You win")
    elif(computer == 2 and you == 1):
        print("You win")
    elif(computer == 2 and you == 3): 
        print("You lose")
    elif(computer == 3 and you == 1):
        print("You lose")
    elif(computer == 3 and you == 2):
        print("You win")
    else:
        print("Something went wrong")
# This is the shortend code to use which work's same as the above one
# if((computer - you) == 1 or (computer - you) == -2):
#     print("You win!")
# else:
#     print("You lose!")