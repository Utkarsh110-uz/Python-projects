from tkinter import *
import tkinter as tk

root = Tk() # Here we made the main window and given below are the normal things like app name and about the app background color
root.title("TO-DO List")
root.config(bg="#E6BDB5")

main_heading = Label(root, text="TO-DO List", background="#E6BDB5", foreground="Black", font=("Arial Bold", 20))
main_heading.pack()

frame = Frame(root) # Here we used frame because we used grid also
frame.pack(pady=50)

Label(frame, text='Entre Task Here or q to exit').grid(row=0) # Here we are taking input from the user
e1 = Entry(frame)
e1.grid(row=0, column=1, padx=20, pady=20)

Lb = Listbox(root) # Made a listbox where the user enterd task will be shown
Lb.pack()
# In this below function we can see the logic of addind task
def task_add_function():
    add_task = e1.get()
    if add_task and add_task != "q":
        with open("task.txt", "a") as f:
            f.write(f"{add_task}\n")
        Lb.insert(END, add_task)
    e1.delete(0, END)
# In the below function we can see the logic of removing task
def remove_task_function():
    selected = Lb.curselection()
    remove_task = Lb.delete(selected)

task_add_button = tk.Button(root, text="Add Task", width=30, command=task_add_function)
task_add_button.pack() # Here we created add task button

remove_task_button = tk.Button(root, text="Remove Task", width=30, command=remove_task_function)
remove_task_button.pack() # Here we created remove task button

exit_button = tk.Button(root, text="Exit", width=30, command=root.destroy)
exit_button.pack() # Here we created exit button

root.mainloop() # Here we closed the main window