import socket
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

SERVER = None
IP_ADDRESS = "127.0.0.1"
PORT = 8050


def setup():
    global SERVER
    global IP_ADDRESS
    global PORT

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


setup()

window = Tk()
window.title("Music Window")
window.geometry("300×300")
window.configure(bg="Dodgerblue")

selectLabel = Label(window, text="Select a song",
                    bg="Dodgerblue", font=("Calibri", 0))
selectLabel.place(x=2, y=1)

listBox = Listbox(window, height=10, width=39, activestyle="dotbox",
                  bg="Dodgerblue", borderwidth=2, font=("Calibri", 0))
listBox.place(x=10, y=10)

scrollBar1 = Scrollbar(listBox)
scrollBar1.place(relheight=1, relx=1)
scrollBar1.config(command=listBox.yview)

playButton = Button(window, text="Play", width=10, bd=1,
                    bg="Dodgerblue", font=("Calibri", 0))
playButton.place(x=30, y=200)

stopButton = Button(window, text="Stop", width=10, bd=1,
                    bg="Dodgerblue", font=("Calibri", 0))
stopButton.place(x=200, y=200)

uploadButton = Button(window, text="Upload", width=10,
                      bd=1,  bg="Dodgerblue", font=("Calibri", 0))
uploadButton.place(x=30, y=250)

downloadButton = Button(window, text="Download", width=10,
                        bd=1,  bg="Dodgerblue", font=("Calibri", 0))
downloadButton.place(x=200, y=250)

infoLabel = Label(window, text="", fg="Blue", font=("Calibri", 10))
infoLabel.place(x=4, y=280)

window.mainloop()
