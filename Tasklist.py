'''
first create a folder from the user's name
and in that create a folder from the name the user will give you
and then create files in them 

features:
1. add more files
2. remove files.
3. rename files names.
4. rename folder name.
5. edit the exsisting file.
6. view the exsisting folders.
7. view the exsisting files.
8. clear files.
9. clear folders.
10. add more foldes.
11. you can moves files from one folder to another folder.
'''
import os
import shutil

print("Make folder in easy steps")

username = input("Enter your username: ")
if (username in os.listdir("D:/Code")):
    print("You already have many folders")
else:
    os.mkdir(f"D:/Code/{username}")
    print("Your folder is created go on check on")

print('''You can do the following things with your folder:
1. Press '1' to makr more files in your folder
2. Press '2' to remove files from your folder''')

ask = input("Enter number of your choice: ")

if("1" in ask):
    folder_no = int(input("How many folder you want to make: "))
    i = 0
    while(i<folder_no):
        folder_name = input("Enter folder name: ")
        os.mkdir(f"D:/Code/{username}/{folder_name}")
        i = i + 1
else:
    print("Something went wrong")