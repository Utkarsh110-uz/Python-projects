# Importing modules
from tkinter import *
from tkinter import ttk
import time

# Creating main window
root = Tk()

# Main window related operations
root.title("Digital Clock")
root.geometry("300x200")
root.config(bg="#0d0d0d")

# Defined functions

# Time and date update function
def update_time():
    current_time = time.strftime("%H:%M:%S %p")
    current_date = time.strftime("%A, %d %B %Y")

    time_label.config(text=current_time)
    date_label.config(text=current_date)

    root.after(1000, update_time)

# Buttons styles
btn_style = ttk.Style()
btn_style.theme_use("default")
btn_style.configure("Time.TButton", background="#00ff99", foreground="#0d0d0d", font=("Courier New", 15, "bold"), focuscolor="none")
btn_style.map("Time.TButton", background=[("active", "#00ff99")], foreground=[("active", "#0d0d0d")])

# Time label
time_label = Label(root, bg="#0d0d0d", fg="#00ff99", font=("Courier New", 28, "bold"))
time_label.pack(pady=5)

# Date label
date_label = Label(root, bg="#0d0d0d", fg="#00cc77", font=("Courier New", 14))
date_label.pack(pady=5)

# Button
quit_btn = ttk.Button(root, text="Quit", command=root.destroy, style="Time.TButton")
quit_btn.pack(pady=5)

update_time() # Function call

# Closing main window
root.mainloop()