import tkinter


window = tkinter.Tk()
window.title("Welcome to Tkinter")
window.minsize(500, 500)
button = tkinter.Button(window, text="Click on me")
button.pack()
label = tkinter.Label(window, text="I am a label", font=('Arial', 25, 'bold')
label.pack()


window.mainloop()                     
