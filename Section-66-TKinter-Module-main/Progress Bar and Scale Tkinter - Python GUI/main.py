from tkinter import *
from tkinter import ttk


window = Tk()
progressbar = ttk.Progressbar(window, orient=HORIZONTAL, length=250)
progressbar.pack()
progressbar.config(mode='indeterminate')
progressbar.start()
progressbar.stop()
progressbar.config(mode='determinate', maximum=10.0, value=2.2)
progressbar.config(value=8.0)
progressbar.step(5)
bar_value = DoubleVar()
progressbar.config(variable=bar_value)
scale = ttk.Scale(window, orient=HORIZONTAL, length=500, variable=bar_value, from_=0.0, to=10.0)
scale.pack()
scale.set(5)

window.mainloop()