from tkinter import *
import tkinter as tk

root = Tk()
root.title("TO-DO List")
root.config(bg="#E6BDB5")

main_heading = Label(root, text="TO-DO List", background="#E6BDB5", foreground="Black", font=("Arial Bold", 20))
main_heading.pack()

frame = Frame(root)
frame.pack(pady=50)

Label(frame, text='Entre Task Here or q to exit').grid(row=0)
e1 = Entry(frame)
e1.grid(row=0, column=1, padx=20, pady=20)

Lb = Listbox(root)
Lb.pack()

def task_add_function():
    add_task = e1.get()
    if add_task and add_task != "q":
        with open("task.txt", "a") as f:
            f.write(f"{add_task}\n")
        Lb.insert(END, add_task)
    e1.delete(0, END)

def remove_task_function():
    selected = Lb.curselection()
    remove_task = Lb.delete(selected)

task_add_button = tk.Button(root, text="Add Task", width=30, command=task_add_function)
task_add_button.pack()

remove_task_button = tk.Button(root, text="Remove Task", width=30, command=remove_task_function)
remove_task_button.pack()

exit_button = tk.Button(root, text="Exit", width=30, command=root.destroy)
exit_button.pack()

root.mainloop()