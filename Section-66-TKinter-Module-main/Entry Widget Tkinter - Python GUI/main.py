from tkinter import *
from tkinter import ttk


window = Tk()
entry = ttk.Entry(window, width=20)
entry.pack()
entry.insert(0, 'Hello Elshad')
entry.config(show='?')


window.mainloop()