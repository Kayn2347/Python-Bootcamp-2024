from tkinter import *


main_window = Tk()
canvas = Canvas(main_window)
canvas.pack()
canvas.config(width=640, height=480)
line = canvas.create_line(150, 350, 470, 110, fill='red', width=4)
canvas.itemconfig(line, fill='blue')
print(canvas.coords(line))
canvas.coords(line, 0, 0, 300, 200, 500, 600)
canvas.itemconfig(line, smooth=True)
canvas.itemconfig(line, splinesteps=3)
canvas.delete(line)

rect = canvas.create_rectangle(150, 110, 470, 350)
canvas.itemconfig(rect, fill='green')
oval = canvas.create_oval(150, 110, 470, 350)
canvas.itemconfig(oval, fill='red')
arc = canvas.create_arc(150, 5, 470, 210)
canvas.itemconfig(arc, start=0, extent=180, fill='yellow')

polygon = canvas.create_polygon(150, 360, 320, 470, 470, 360, fill='blue')
text = canvas.create_text(320, 240, text='AppMillers', font=('Arial', 32, 'bold'))

logo = PhotoImage(file='python_logo.gif')
image = canvas.create_image(320, 240, image=logo)
canvas.lift(text)
canvas.lower(image, text)

button = Button(canvas, text= 'OK')
canvas.create_window(320, 80, window=button)


main_window.mainloop()