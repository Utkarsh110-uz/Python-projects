# Importing module
from tkinter import *

# Initializing main window
window = Tk()

# Window related operations
window.title("Calculator")
window.geometry("600x400")
window.config(bg="#FCD8CF")

# Initializing functions
def add():
    n1 = int(number1.get())
    n2 = int(number2.get())
    output_label.config(text=n1 + n2)

def sub():
    n1 = int(number1.get())
    n2 = int(number2.get())
    output_label.config(text=n1 - n2)

def mul():
    n1 = int(number1.get())
    n2 = int(number2.get())
    output_label.config(text=n1 * n2)

def div():
    try:
        n1 = int(number1.get())
        n2 = int(number2.get())
        output_label.config(text=n1 / n2)
    except ZeroDivisionError:
        output_label.config(text="You are dividing number with 0 which is not possible")

def delete_all():
    number1.delete(0, END)
    number2.delete(0, END)
    output_label.config(text="Output will be seen here")

# Initializing label
output_label = Label(window, text="Output will be seen here", font=("Devanagari Sangam MN", 20, "bold"), bg="#FCD8CF", fg="Black")
output_label.pack(pady=2)

# Initializing inputs
number1 = Entry(width=10)
number1.pack(pady=2)

number2 = Entry(width=10)
number2.pack(pady=2)

# Initializing buttons
add_button = Button(window, text="+", command=add, width=5)
add_button.pack(pady=2)

sub_button = Button(window, text="-", command=sub, width=5)
sub_button.pack(pady=2)

mul_button = Button(window, text="*", command=mul, width=5)
mul_button.pack(pady=2)

div_button = Button(window, text="/", command=div, width=5)
div_button.pack(pady=2)

delete_button = Button(window, text="Delete", command=delete_all, width=5)
delete_button.pack(pady=2)

exit_button = Button(window, text="Quit", command=window.destroy, width=5)
exit_button.pack()

window.mainloop()