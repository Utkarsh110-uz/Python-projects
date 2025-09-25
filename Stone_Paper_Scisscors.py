# Stone Paper Scisscors game:
# This game also uses same logic using snake water gun game

import random

computer = random.choice([1, 2, 3])
youstr = input("Enter your move: ")
dict = {"stone": 1, "paper": 2, "scisscors": 3}
revdict = {1: "stone", 2: "paper", 3: "scisscors"}
you = dict[youstr]
print(f"You chose: {revdict[you]}\nComputer chose: {revdict[computer]}")
if(computer == you):
    print("It's a draw")
else:
    if(computer == 1 and you == 2): # 1
        print("You win")
    elif(computer == 1 and you == 3): # 2
        print("You lose")
    elif(computer == 2 and you == 1): # -1
        print("You lose")
    elif(computer == 2 and you == 3): # 1
        print("You win")
    elif(computer == 3 and you == 1): # -2
        print("You win")
    elif(computer == 3 and you == 2): # -1
        print("You lose")
    else:
        print("Something went wrong")

# if((computer - you) == 1 or (computer - you) == -2):
#     print("You win")
# else:
#     print("You lose")