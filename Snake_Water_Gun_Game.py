# Snake Water Gun Game:
# Snake = 1, Water = 2, Gun = 3 

import random

computer = random.choice([1, 2, 3])

youstr = input("Enter your move: ")
dict = {"s": 1, "w": 2, "g": 3}
revdict = {1: "Snake", 2: "Water", 3: "Gun"}
you = dict[youstr]

print(f"You chose: {revdict[you]}\nComputer chose: {revdict[computer]}")

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

# if((computer - you) == 1 or (computer - you) == -2):
#     print("You win!")
# else:
#     print("You lose!")