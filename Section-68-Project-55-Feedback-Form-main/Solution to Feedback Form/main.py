from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Feedback:
    def __init__(self, master):
        master.title('AppMillers Online Courses')
        master.resizable(False, False)
        master.configure(background='#ECECEC')
        self.style = ttk.Style()
        self.style.configure('TLabel', background='#ECECEC', font=('Arial', 11))
        self.style.configure('Header.TLabel', font=('Arial', 18, 'bold'))

        self.header_frame = ttk.Frame(master)
        self.header_frame.pack()


        self.logo = PhotoImage(file="appmillers_logo.gif")
        ttk.Label(self.header_frame, image=self.logo).grid(row=0, column=0, rowspan=2)
        ttk.Label(self.header_frame, text="Thanks for joining us!", style ='Header.TLabel').grid(row=0, column=1)
        ttk.Label(self.header_frame, wraplength=300, text='We are glad you chose Appmillers for your online study. ' 
                                           'Please tell us what you thought about our online courses').grid(row=1, column=1)

        self.content_frame = ttk.Frame(master)
        self.content_frame.pack()

        ttk.Label(self.content_frame, text="Name:").grid(row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.content_frame, text="Email:").grid(row=0, column=1, padx=5, sticky='sw')
        ttk.Label(self.content_frame, text="Comments:").grid(row=2, column=0, padx=5, sticky='sw')
        self.name_entry = ttk.Entry(self.content_frame, width=20)
        self.email_entry = ttk.Entry(self.content_frame, width=20)
        self.comment_text = Text(self.content_frame, width=50, height=10, font=('Arial', 10))

        self.name_entry.grid(row=1, column=0, padx=5)
        self.email_entry.grid(row=1, column=1, padx=5)
        self.comment_text.grid(row=3, column=0, columnspan=2, padx=5)

        ttk.Button(self.content_frame, text='Submit', command=self.submit).grid(row=4, column=0, padx=5, sticky='e')
        ttk.Button(self.content_frame, text='Clear', command=self.clear).grid(row=4, column=1, padx=5, sticky='w')

    def clear(self):
        self.name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.comment_text.delete(1.0, 'end')

    def submit(self):
        print(f'Name: {self.name_entry.get()}')
        print(f'Email: {self.email_entry.get()}')
        print(f'Email: {self.comment_text.get("1.0", "end")}')
        self.clear()
        messagebox.showinfo(title="Online Course Feedback", message='Comments submitted!')

def main():
    main_window = Tk()
    feedback = Feedback(main_window)
    main_window.mainloop()


if __name__ == "__main__":
    main()