from tkinter import *
from tkinter import ttk

window = Tk()
frame = ttk.Frame(window)
frame.pack()
frame.config(height=150, width=300)
frame.config(relief=RIDGE)
ttk.Button(frame, text='Click me').grid()
frame.config(padding=(30,15))
ttk.LabelFrame(window, height=150, width=300, text="My Label Frame").pack()


window.mainloop()