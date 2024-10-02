from tkinter import *
from tkinter import ttk

main_window = Tk()
notebook = ttk.Notebook(main_window)
notebook.pack()
first_frame = ttk.Frame(notebook)
second_frame = ttk.Frame(notebook)
notebook.add(first_frame, text='First Label')
notebook.add(second_frame, text='Second Label')
ttk.Button(first_frame, text='Click me').pack()
third_frame = ttk.Frame(notebook)
notebook.insert(0, third_frame, text='Third Label')
notebook.forget(0)
notebook.add(third_frame, text='Third Label')
print(notebook.select())
print(notebook.index(notebook.select()))
notebook.select(1)
notebook.tab(1, state='hidden')
notebook.tab(1, state='normal')
# notebook.tab(1, state='disabled')
print(notebook.tab(0))


main_window.mainloop()