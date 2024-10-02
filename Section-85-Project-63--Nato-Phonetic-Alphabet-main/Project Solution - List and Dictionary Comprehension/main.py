from tkinter import *
from tkinter import messagebox

import pandas


class MainInterface:
    def __init__(self, root, data):
        # TODO 1. Create a dictionary in CSV format:
        self.phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
        root.title("NATO Phonetic Alphabet")
        root.geometry("500x200+500+200")
        root.config(bg="#33373d")
        root.resizable(0, 0)
        self.name = StringVar()


        # Entries Frame
        self.entries_frame = Frame(root, bg="#33373d")
        self.entries_frame.pack(side=TOP, fill=X)
        self.title = Label(self.entries_frame, text="NATO phonetic alphabet", font=("Calibri", 18, "bold"), bg="#33373d",
                      fg="white")
        self.title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
        # name label and entry field
        self.name_label = Label(self.entries_frame, text="Name", font=("Calibri", 16), bg="#33373d", fg="white")
        self.name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_name = Entry(self.entries_frame, textvariable=self.name, font=("Calibri", 16), width=30)
        self.entry_name.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Buttons
        self.button_frame = Frame(self.entries_frame, bg="#555C67")
        self.button_frame.grid(row=6, column=0, columnspan=5, padx=10, pady=10, sticky="w")
        self.button_add = Button(self.button_frame, text="Submit", command=self.show_result, width=15,
                                 font=("Calibri", 16, "bold"), bd=0).grid(row=0, column=0)

    def show_result(self):
        # TODO 2 Show a list of the phonetic code words from a word that is inserted.
        try:
            output_list = [self.phonetic_dict[letter] for letter in self.name.get()]
        except KeyError:
            messagebox.showerror("Error", "Please enter name in capital letters")
        messagebox.showinfo("Info", output_list)



if __name__ == '__main__':
    main_window = Tk()
    data = pandas.read_csv("nato_phonetics.csv")
    em = MainInterface(main_window, data)


    main_window.mainloop()




