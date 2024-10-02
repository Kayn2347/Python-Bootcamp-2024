from tkinter import *
from tkinter import ttk
from random_text import SAMPLE_TEXT


main_window = Tk()
text = Text(main_window, width=50, height=15, wrap='word')
text.grid(row=0, column=0)
text.insert('1.0', SAMPLE_TEXT)
scroll_bar = ttk.Scrollbar(main_window, orient=VERTICAL, command=text.yview)
scroll_bar.grid(row=0, column=1, sticky='ns')
text.config(yscrollcommand=scroll_bar.set)


main_window.mainloop()