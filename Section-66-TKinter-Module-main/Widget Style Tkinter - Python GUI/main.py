from tkinter import *
from tkinter import ttk


main_window = Tk()
button1 = ttk.Button(main_window, text="Button 1")
button2 = ttk.Button(main_window, text="Button 2")
button1.pack()
button2.pack()
style = ttk.Style()
print(style.theme_names())
print(style.theme_use())
# style.theme_use('classic')
print(button1.winfo_class())
style.configure('TButton', foreground='red')
style.configure('test.TButton', foreground='green', font=('Arial', 20, 'bold'))
button2.configure(style='test.TButton')
style.map('test.TButton', foreground=[('pressed','blue'), ('disabled', 'grey')])
button2.state(['disabled'])

main_window.mainloop()