from tkinter import *
import tkinter as tk
root = Tk()
root.title("Calculator app")
root.config(bg="#D2C6F5")

heading = Label(root, text= "Welcome to EasyCount", font=("Arial Bold", 20),background="#D2C6F5", foreground="#2B024C")
heading.pack(pady=10)

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text="Number 1", foreground="black", font=("Arial", 15)).grid(row=0, padx=10, pady=10)
Label(frame, text="Number 2", foreground="black", font=("Arial", 15)).grid(row=1, padx=10, pady=10)
e1 = Entry(frame)
e2 = Entry(frame)
e1.grid(row=0, column=1, padx=10, pady=10)
e2.grid(row=1, column=1, padx=10, pady=10)

lb = Listbox(root, bg="#D2C6F5", fg="#1F0600", font=("Arial Bold", 15), borderwidth="0", highlightbackground="#D2C6F5", highlightcolor="#D2C6F5")
lb.insert(1, "Add = (+)")
lb.insert(2, "Subtract = (-)")
lb.insert(3, "Multiply = (*)")
lb.insert(4, "Divide = (/)")
lb.pack(pady=10)

result_label = Label(root, text="The result will be shown here", font=("Arial", 15), bg="#D2C6F5")
result_label.pack(pady=5)

def calculate():
    try: 
        num1 = float(e1.get())
        num2 = float(e2.get())

        selected = lb.curselection()
        if not selected:
            result_label.config(text="Please select the operation",font=("Arial", 15), bg="#D2C6F5")

        operation = lb.get(selected)

        if ("Add" in operation):
            result = num1 + num2
        elif("Subtract" in operation):
            result = num1 - num2
        elif("Multiply" in operation):
            result = num1 * num2
        elif("Divide" in operation):
            if(num2 == 0):
                result_label.config(text="Zero division error", font=("Arial, 15"), bg="#D2C6F5")
                return
            result = num1 / num2
        else:
            result_label.config(text="Unknown operation", font=("Arial, 15"), bg="#D2C6F5")
            return
        
        result_label.config(text = f"Result is: {result}", font=("Arial, 15"), bg="#D2C6F5")

    except ValueError:
        result_label.config(text="Please enter a valid number", font=("Arial", 15), bg="#D2C6F5")

calculator_button = Button(root, text="Calculate", command=calculate, bg="#D5EDC2", font=("Arial Bold", 12))
calculator_button.pack(pady=10)

button = tk.Button(root, text="Exit Program", width=60, command=root.destroy, background="#EB6565", font=("Arial Bold", 12))
button.pack(pady=10)

root.mainloop()