from tkinter import *
from os import system

window = Tk()

window.title("Sample GUI")
window.geometry("500x300")
window.config(bg="lightblue")

def download_content():
    content = user_input.get()
    system(f"# yt-dlp -x --audio-format mp3 --audio-quality 0 {content}")

def clear_content():
    user_input.delete(0, END)

content = Label(window, text="Download videos in one click", bg="lightblue", font=("Arial", 20, "bold"))
content.pack(pady=5)

user_input = Entry(width=60)
user_input.pack(pady=5)

download_button = Button(window, text="Download", command=download_content, width=12)
download_button.pack(pady=5)

clear_button = Button(window, text="Clear", command=clear_content, width=12)
clear_button.pack(pady=5)

quit_button = Button(window, text="Quit", command=window.quit, width=12)
quit_button.pack(pady=5)

window.mainloop()

# yt-dlp -x --audio-format mp3 --audio-quality 0 <youtube_url>.