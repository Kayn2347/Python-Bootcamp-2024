from tkinter import *
from tkinter import ttk


main_window = Tk()
main_window.geometry("640x480+500+200")

ttk.Label(main_window, text='Sample Label1').place(x=100, y=100, width=100, height=50)
ttk.Label(main_window, text='Sample Label2').place(relx=0.5, rely=0.5, anchor='center',
                                                   relwidth=0.5, relheight=0.5
ttk.Label(main_window, text='Sample Label3').place(relx=0.5, x=100, rely=0.5, y=50)
ttk.Label(main_window, text='Sample Label4').place(relx=1, x=5, y=5, anchor='ne')


main_window.mainloop()
