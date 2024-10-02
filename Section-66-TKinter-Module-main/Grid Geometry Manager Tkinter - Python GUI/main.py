from tkinter import *
from tkinter import ttk


main_window = Tk()
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=3)

ttk.Label(main_window, text='Sample Label1').grid(row=0, column=0, stick='nsew')
ttk.Label(main_window, text='Sample Label2').grid(row=0, column=1, stick='nsew')
ttk.Label(main_window, text='Sample Label3').grid(row=1, column=0, columnspan=2, stick='nsew')
ttk.Label(main_window, text='Sample Label4').grid(row=0, column=2, rowspan=2, stick='nsew')


main_window.mainloop()
