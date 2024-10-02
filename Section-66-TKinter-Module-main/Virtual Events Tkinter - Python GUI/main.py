from tkinter import *
from tkinter import ttk


main_window = Tk()

entry = ttk.Entry()
entry.pack()
entry.bind("<<Copy>>", lamba e: print("Copying.."))
entry.bind("<<Paste>>", lamba e: print("Pasting.."))
entry.event_add("<<EvenNumber>>", "2", "4", "6", "8")
entry.bind("<<EvenNumber>>", lambda e: print("Even number.."))
# print(entry.event_info("<<EvenNumber>>")
entry.event_generate("<<EvenNumber>>")
entry.event_delete("<<EvenNumber>>")

      

main_window.mainloop()
