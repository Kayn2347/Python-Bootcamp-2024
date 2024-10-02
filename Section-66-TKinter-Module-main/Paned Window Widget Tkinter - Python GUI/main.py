from tkinter import *
from tkinter import ttk

main_window = Tk()
paned_window = ttk.Panedwindow(main_window, orient=HORIZONTAL)
paned_window.pack(fill=BOTH, expand=True)
first_frame = ttk.Frame(paned_window, width=100, height=300, relief=SUNKEN)
second_frame = ttk.Frame(paned_window, width=350, height=350, relief=SUNKEN)
paned_window.add(first_frame, weight=1)
paned_window.add(second_frame, weight=4)
third_frame = ttk.Frame(paned_window, width=50, height=350, relief=SUNKEN)
paned_window.insert(1, third_frame)
paned_window.forget(1)



main_window.mainloop()