# *Note this code is under development and not yet finished can be used when it is finished.*
import os
import shutil

username = input("Enter your username here: ")
if not (os.path.exists(f"D:/Code/{username}")):
    os.mkdir(f"D:/Code/{username}")
    print("Folder Created")
else:
    print("username already exsist and your folders are:")
    folders = os.listdir(f"D:/Code/{username}")
    for folder in folders:
        print(folder)

while True:
    print("-----------\n1. Press 1 to add folders\n2. Press 2 to add files\n3. Press 3 to remove folders\n4. Press 4 to remove files\n5. Press 5 to rename file name\n6. Press 6 to rename folder name\n7. Press 7 to view the exsisting file\n8. Press 8 to view the exsisting folder\n9. Press 9 to edit the exsisting file\n10. Press 10 to clear files\n11. Press 11 to clear folders\n12. Press 12 to change the location of the folders and files\n13. "
    "Press 13 to exit the program\n-----------")
    ask = input("Enter number to chose the operation: ")

    if("1" in ask):
        folder_name = input("Enter folder name: ")
        os.mkdir(f"D:/Code/{username}/{folder_name}")
        print("Folder created successfully")

    elif("2" in ask):
        ask_fn = input("Enter folder name in which you want to create file: ")
        file_name = input("Enter file name: ")
        while(data := input("Enter information here or 'q' to quit: ")) != "q":
            with open(f"D:/Code/{username}/{folder_name}/{file_name}.txt", "a") as f:
                f.write(f"{data}\n")
        print("File created successfully")

    elif("3" in ask):
        rem_folder = input("Enter the name of the folder you want to delete: ")
        shutil.rmtree(f"D:/Code/{username}/{rem_folder}")
        print("Folder deleted successfully")

    elif("4" in ask):
        folder_name = input("Enter folder name: ")
        rem_file = input("Enter file name here: ")
        os.remove(f"D:/Code/{username}/{folder_name}/{rem_file}")
        print("File deleted successfully")

    elif("13" in ask):
        print("Exit made")
        break

import random
computer = random.choice([1,2,3])
youstr = input("Enter your move here: ")
dict = {"s": 1, "w": 2, "g": 3}
revdict = {1: "Snake", 2: "Water", 3: "Gun"}
you = dict[youstr]
print(f"You chose: {revdict[you]}\nComputer chose: {revdict[computer]}")