from tkinter import *


main_window = Tk()
main_window.option_add("*tearOff", False)
menu_bar = Menu(main_window)
main_window.config(menu=menu_bar)
file = Menu(menu_bar)
edit = Menu(menu_bar)
help_ = Menu(menu_bar)
menu_bar.add_cascade(menu=file, label='File')
menu_bar.add_cascade(menu=edit, label='Edit')
menu_bar.add_cascade(menu=help_, label='Help')


def new():
    print("New File")


def open():
    print("Opening file..")


file.add_command(label='New', command=new)
file.add_separator()
file.add_command(label="Open...", command=open)
file.entryconfig('New', accelerator='Cmd+N')
logo = PhotoImage(file="python.gif").subsample(6, 6)
file.entryconfig('Open...', image=logo, compound='left')
file.entryconfig('Open...', state='disabled')
file.add_separator()
save = Menu(file)
file.add_cascade(menu=save, label='Save')


def saveas():
    print('Saving the file')


save.add_command(label='Save as', command=saveas)
save.add_command(label='Save All')

choice =IntVar()
edit.add_radiobutton(label='One', variable=choice, value=1)
edit.add_radiobutton(label='Two', variable=choice, value=2)
edit.add_radiobutton(label='Three', variable=choice, value=3)


main_window.mainloop()

