from tkinter import *
import tkinter as tk
root = Tk()
root.title("Calculator")

heading = Label(root, text= "Welcome to the Calculator", background="#98E1ED", foreground="black")
heading.pack(pady=10)

button = tk.Button(root, text="Exit Program", width=60, command=root.destroy, background="#EB6565")
button.pack(pady=10)

frame = Frame(root)
frame.pack(pady=5)

Label(frame, text="Number 1", foreground="#0C3EF2").grid(row=0, padx=5, pady=10)
Label(frame, text="Number 2", foreground="#0C3EF2").grid(row=1, padx=5, pady=10)
e1 = Entry(frame)
e2 = Entry(frame)
e1.grid(row=0, column=1, padx=5, pady=3)
e2.grid(row=1, column=1, padx=5, pady=3)

lb = Listbox(root)
lb.insert(1, "Add = +")
lb.insert(2, "Subtract = -")
lb.insert(3, "Multiply = *")
lb.insert(4, "Divide = /")
lb.pack(pady=20)

result_label = Label(root, text="The result will be shown here", font=("Arial", 12), bg="#CED6E0")
result_label.pack(pady=10)

def calculate():
    try: 
        num1 = float(e1.get())
        num2 = float(e2.get())

        selected = lb.curselection()
        if not selected:
            result_label.config(text="Please select the operation", bg="#CED6E0")

        operation = lb.get(selected)

        if ("Add" in operation):
            result = num1 + num2
        elif("Subtract" in operation):
            result = num1 - num2
        elif("Multiply" in operation):
            result = num1 * num2
        elif("Divide" in operation):
            if(num2 == 0):
                result_label.config(text="Zero division error", bg="#CED6E0")
                return
            result = num1 / num2
        else:
            result_label.config(text="Unknown operation", bg="#8BF0CB")
            return
        
        result_label.config(text = f"Result is: {result}", bg="#CED6E0")

    except ValueError:
        result_label.config(text="Please enter a valid number", bg="#CED6E0")

calculator_button = Button(root, text="Calculate", command=calculate, bg="#D5EDC2")
calculator_button.pack(pady=10)

feedback = Text(root, width=35, height= 4, bg="#F2ECE6")
feedback.pack()
feedback.insert(END, "Enter your feedback here:")

root.mainloop()