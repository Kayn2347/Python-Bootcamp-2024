from tkinter import *
from tkinter import  ttk

window = Tk()
label = ttk.Label(window,text='Hello TK')
label.pack()
label.config(text="Hello Tkinter, My name is Elshad and I am studying Python for Everyone Course")
label.config(wraplength=200)
label.config(justify=CENTER)
label.config(foreground='red')
label.config(font=('Arial', 20, 'bold'))


logo = PhotoImage(file='python.gif')
label.img = logo
label.config(image=label.img)

label.config(compound='bottom')

window.mainloop()