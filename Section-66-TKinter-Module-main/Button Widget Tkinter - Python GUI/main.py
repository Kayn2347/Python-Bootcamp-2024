from tkinter import *
from tkinter import  ttk

window = Tk()
button = ttk.Button(window, text="Click me")
button.pack()


def button_press():
    print("The button is pressed")


button.config(command=button_press)
logo = PhotoImage(file='python.gif')
small_logo = logo.subsample(3, 3)
button.config(image=small_logo, compound=LEFT)

window.mainloop()
