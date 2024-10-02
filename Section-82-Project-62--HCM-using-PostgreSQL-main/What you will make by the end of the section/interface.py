from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database
from details_interface import DetailInterface


class MainInterface:
    def __init__(self, root):
        self.db = Database()
        root.title("Employee Management System")
        root.geometry("1920x1080+0+0")
        root.config(bg="#555C67")
        root.state("zoomed")
        self.root = root
        # Variables
        self.name = StringVar()
        self.age = StringVar()
        self.dob = StringVar()
        self.gender = StringVar()
        self.email = StringVar()
        self.contact = StringVar()

        # Entries Frame
        self.entries_frame = Frame(root, bg="#535c68")
        self.entries_frame.pack(side=TOP, fill=X)
        self.title = Label(self.entries_frame, text="Employee Management System", font=("Calibri", 18, "bold"), bg="#535c68",
                      fg="white")
        self.title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
        # name label and entry field
        self.name_label = Label(self.entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
        self.name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_name = Entry(self.entries_frame, textvariable=self.name, font=("Calibri", 16), width=30)
        self.entry_name.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        # age label and entry field
        self.age_label = Label(self.entries_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
        self.age_label.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.entry_age = Entry(self.entries_frame, textvariable=self.age, font=("Calibri", 16), width=30)
        self.entry_age.grid(row=1, column=3, padx=10, pady=10, sticky="w")
        # dob label and entry field
        self.dob_label = Label(self.entries_frame, text="DOB", font=("Calibri", 16), bg="#535c68", fg="white")
        self.dob_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_dob = Entry(self.entries_frame, textvariable=self.dob, font=("Calibri", 16), width=30)
        self.entry_dob.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        # email label and entry field
        self.email_label = Label(self.entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
        self.email_label.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.entry_email = Entry(self.entries_frame, textvariable=self.email, font=("Calibri", 16), width=30)
        self.entry_email.grid(row=2, column=3, padx=10, pady=10, sticky="w")
        # gender label and combobox
        self.gender_label = Label(self.entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
        self.gender_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.combo_gender = ttk.Combobox(self.entries_frame, font=("Calibri", 16), width=28, textvariable=self.gender, state="readonly")
        self.combo_gender['values'] = ("Male", "Female")
        self.combo_gender.grid(row=3, column=1, padx=10, sticky="w")
        # contact label and entry field
        self.contact_label = Label(self.entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
        self.contact_label.grid(row=3, column=2, padx=10, pady=10, sticky="w")
        self.entry_contact = Entry(self.entries_frame, textvariable=self.contact, font=("Calibri", 16), width=30)
        self.entry_contact.grid(row=3, column=3, padx=10, sticky="w")
        # address label and text field
        self.address_label = Label(self.entries_frame, text="Address", font=("Calibri", 16), bg="#535c68", fg="white")
        self.address_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.text_address = Text(self.entries_frame, width=85, height=5, font=("Calibri", 16))
        self.text_address.grid(row=5, column=0, columnspan=5, padx=10, sticky="w")

        # Buttons
        self.button_frame = Frame(self.entries_frame, bg="#555C67")
        self.button_frame.grid(row=6, column=0, columnspan=5, padx=10, pady=10, sticky="w")
        self.button_add = Button(self.button_frame, command=self.add_employee, text="Add Details", width=15,
                                 font=("Calibri", 16, "bold"), bd=0).grid(row=0, column=0)
        self.button_edit = Button(self.button_frame, command=self.update_employee, text="Update Details", width=15,
                                  font=("Calibri", 16, "bold"), bd=0).grid(row=0, column=1, padx=10)
        self.button_delete = Button(self.button_frame, command=self.delete_employee, text="Delete Details", width=15,
                                    font=("Calibri", 16, "bold"), bd=0).grid(row=0, column=2, padx=10)
        self.button_clear = Button(self.button_frame, command=self.clear_all, text="Clear Details", width=15,
                                   font=("Calibri", 16, "bold"), bd=0).grid(row=0, column=3, padx=10)
        # New Button
        self.view_details = Button(self.button_frame, command=self.open_details, text="View Details", width=15,
                                   font=("Calibri", 16, "bold"), bd=0).grid(row=0, column=4, columnspan=3, padx=10)

        # Table Frame
        self.tree_frame = Frame(root)
        # self.tree_frame.place(x=0, y=480, width=1500, height=520)
        self.tree_frame.pack(side=BOTTOM, fill=X, pady=30)
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=('Calibri', 18),
                        rowheight=50)  # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 18))  # Modify the font of the headings
        self.tv = ttk.Treeview(self.tree_frame, columns=(1, 2, 3, 4, 5), style="mystyle.Treeview")
        self.tv.heading("1", text="ID")
        self.tv.column("1", width=2)
        self.tv.heading("2", text="Name")
        self.tv.heading("3", text="Age")
        self.tv.column("3", width=5)
        self.tv.heading("4", text="D.O.B")
        self.tv.column("4", width=10)
        self.tv.heading("5", text="Gender")


        self.tv['show'] = 'headings'
        self.tv.bind("<ButtonRelease-1>", self.get_data)
        self.tv.pack(fill=X)

    def get_data(self, event):
        selected_row = self.tv.focus()
        data = self.tv.item(selected_row)
        global row
        row = data["values"]
        # print(row)
        self.name.set(row[1])
        self.age.set(row[2])
        self.dob.set(row[3])
        self.gender.set(row[4])
        self.text_address.delete(1.0, END)
        self.email.set("")
        self.contact.set("")
        self.text_address.delete(1.0, END)

    def display_all(self):
        self.tv.delete(*self.tv.get_children())
        for row in self.db.fetch():
            self.tv.insert("", END, values=row)


    def add_employee(self):
        if self.entry_name.get() == "" or self.entry_age.get() == "" or self.entry_dob.get() == "" or self.entry_email.get() == "" or self.combo_gender.get() == "" or self.entry_contact.get() == "" or self.text_address.get(
                1.0, END) == "":
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return
        self.db.insert(self.entry_name.get(), self.entry_age.get(), self.entry_dob.get(), self.entry_email.get(), self.combo_gender.get(), self.entry_contact.get(),
                  self.text_address.get(
                      1.0, END))
        messagebox.showinfo("Success", "Record Inserted")
        self.clear_all()
        self.display_all()

    def update_employee(self):
        if self.entry_name.get() == "" or self.entry_age.get() == "" or self.entry_dob.get() == "" or self.entry_email.get() == "" or self.combo_gender.get() == "" or self.entry_contact.get() == "" or self.text_address.get(
                1.0, END) == "":
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return
        self.db.update(row[0], self.entry_name.get(), self.entry_age.get(), self.entry_dob.get(), self.entry_email.get(), self.combo_gender.get(),
                  self.entry_contact.get(),
                  self.text_address.get(
                      1.0, END))
        messagebox.showinfo("Success", "Record Update")
        self.clear_all()
        self.display_all()

    def delete_employee(self):
        self.db.remove(row[0])
        self.clear_all()
        self.display_all()

    def clear_all(self):
        self.name.set("")
        self.age.set("")
        self.dob.set("")
        self.gender.set("")
        self.email.set("")
        self.contact.set("")
        self.text_address.delete(1.0, END)

    def open_details(self):
        dt = DetailInterface(self.root)
        details = self.db.fetch_details(row[0])
        for det in details:
            dt.tv.insert("", END, values=det)
        print(details)
        self.email.set(details[0][0])
        self.contact.set(details[0][1])
        self.text_address.delete(1.0, END)
        self.text_address.insert(END, details[0][2])







def main():
    main_window = Tk()
    em = MainInterface(main_window)
    em.display_all()
    main_window.mainloop()



