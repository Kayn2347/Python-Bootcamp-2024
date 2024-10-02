from tkinter import *
from tkinter import ttk


main_window = Tk()
canvas = Canvas(main.window, width=640, height=480, background='red')
canvas.pack()

def mouse_press(event):
    global prev event
    prev_event = event
   print(f"Type: {event.type}")
   print(f"Widget: {event.widget}")
   print(f"Num: {event.num}")
   print(f"x: {event.x}")
    print(f"y: {event.y}")


def draw(event):
    global prev_event
    canvas.create_line(prev_event.x, prev_event.y, event.x, event.y, width=5)
    prev_event = event

canvas.bind("<ButtonPress>", mouse_press
canvas.bind('<B1 -Motion', draw)


main_window.mainloop()
