# *Note this app is under development not yet completed in future i am going to add more functions.*
from tkinter import *
import tkinter as tk
import requests

root = Tk() # Here we are creating the main window
root.title("Image Downloading App")
root.config(bg="#609EEB")

label = Label(root, text="|---Click & Save---|", font=("Arial Bold", 20), bg="#609EEB", fg="#36361C")
label.pack(pady=10) # Here made a label and showed the name of the application nothing else

frame = Frame(root) # Here we used root becasue we are using .grid inside frame window and in root window we used .pack
frame.pack(pady=10)

# Here below we are taking input from the user
Label(frame, text="Enter your URL here:", foreground="black", font=("Arial Bold", 12)).grid(row=0, padx=10, pady=10)
Label(frame, text="Enter file name:", foreground="black", font=("Arial Bold", 12)).grid(row=1, padx=10, pady=10)
e1 = Entry(frame)
e2 = Entry(frame)
e1.grid(row=0, column=1, padx=10, pady=10)
e2.grid(row=1, column=1, padx=10, pady=10)

# Here below we defined the function to download image
def image_download():
    url = e1.get()
    file_name = e2.get()
    response = requests.get(url)
    open(f"{file_name}.jpg", "wb").write(response.content)
    print("image downloaded")

download_button = tk.Button(frame, text="Download", command=image_download, font=("Arial Bold", 15))
download_button.grid(row=2, column=0, columnspan=2, pady=10)

quit_button = tk.Button(frame, text="Quit", command=root.quit, font=("Arial Bold", 15))
quit_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop() # Here we are closing the main window