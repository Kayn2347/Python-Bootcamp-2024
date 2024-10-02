from tkinter import *
from tkinter import ttk


main_window = Tk()


def key_press(event):
    print(f"Type: {event.type}")
    print(f"Widget: {event.widget}")
    print(f"Char: {event.char}")
    print(f"key Symbol: {event.keysym}")
    print(f"Key Code: {event.keycode}")


main_window.bind("<KeyPress>", key_press)

main_window.mainloop()
