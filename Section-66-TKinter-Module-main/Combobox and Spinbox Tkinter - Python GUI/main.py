from tkinter import *
from tkinter import ttk


window = Tk()
week_day = StringVar()
week_cb = ttk.Combobox(window, textvariable=week_day)
week_cb.pack()
week_days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
week_cb.config(values=week_days)

day = StringVar()
Spinbox(window, from_=1, to=30, textvariable=day).pack()



window.mainloop()