from tkinter import *
from tkinter import ttk

window = Tk()
check_button = ttk.Checkbutton(window, text='Agree?')
check_button.pack()
agree = StringVar()
check_button.config(variable=agree, onvalue='Agree', offvalue='Disagree')


def button_pressed():
    print(agree.get())


check_button.config(command=button_pressed)


language = StringVar()
ttk.Radiobutton(window, text='Python', variable=language, value='Python language').pack()
ttk.Radiobutton(window, text='Java', variable=language, value='java').pack()
ttk.Radiobutton(window, text='C++', variable=language, value='c++').pack()

check_button.config(textvariable=language)







window.mainloop()
