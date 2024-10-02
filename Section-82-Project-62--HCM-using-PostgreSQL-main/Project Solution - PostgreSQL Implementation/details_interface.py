from tkinter import *
from tkinter import ttk
from db import Database


class DetailInterface:
    def __init__(self, root):
        self.row = []
        self.db = Database()
        self.detail_window = Toplevel(root)
        self.detail_window.title("Employee Contact Details")
        self.detail_window.geometry("800x300+0+0")
        self.detail_window.config(bg="#555C67")
        self.detail_frame = Frame(self.detail_window, bg="#535c68")
        self.title = Label(self.detail_frame, text="Employee Contact Details", font=("Calibri", 18, "bold"),
                      bg="#535c68",
                      fg="white")
        self.detail_tree_frame = Frame(self.detail_window)

        self.detail_frame.pack(side=TOP, fill=X)

        self.title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
        # Table Frame

        self.detail_tree_frame.pack(side=BOTTOM, fill=BOTH, pady=30)
        style = ttk.Style()

        style.configure("mystyle.Treeview", font=('Calibri', 18),
                             rowheight=50)
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))
        self.tv = ttk.Treeview(self.detail_tree_frame, columns=(1, 2, 3), style="mystyle.Treeview")
        self.tv.heading("1", text="Email")
        self.tv.column("1", width=2)
        self.tv.heading("2", text="Contact No")
        self.tv.heading("3", text="Address")
        self.tv['show'] = 'headings'
        self.tv.pack(fill=BOTH)
        self.tv.delete(*self.tv.get_children())











