from tkinter import *


main_window = Tk()
sub_window = Toplevel(main_window)
sub_window.title("My New Window")
sub_window.attributes("-topmost", True)
# sub_window.state("withdrawn")
sub_window.geometry("640x480+100+100")
# sub_window.resizable(False, False)
sub_window.maxsize(650,500)
sub_window.minsize(300,300)

main_window.destroy()


main_window.mainloop()