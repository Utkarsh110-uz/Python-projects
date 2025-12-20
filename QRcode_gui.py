import qrcode
from tkinter import *

window = Tk()
window.title("QR Code Generator")
window.geometry("500x500")

def Qrcode():
    url = message_input.get().strip()
    file_path = "qrcode.png"
    qr = qrcode.QRCode()
    qr.add_data(url)
    img = qr.make_image()
    img.save(file_path)
    output_label.config(text="QR Code Generated")

message_input = Entry(width=20)
message_input.pack()

output_label = Label(window, text="Enter Message above", font=("Academy Engraved LET", 20))
output_label.pack()

create_button = Button(window, text="Create QR", command=Qrcode)
create_button.pack()

exit_button = Button(window, text="Quit", command=window.destroy)
exit_button.pack()

window.mainloop()