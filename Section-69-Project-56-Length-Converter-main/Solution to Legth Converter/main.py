from tkinter import *
from tkinter import ttk


class Length:
    def __init__(self, master):
        master.title("Length Converter: Mile -> KM")
        master.resizable(width=False, height=False)
        self.frm_entry = ttk.Frame(master=master)
        self.mile_entry = ttk.Entry(master=self.frm_entry, width=10)
        self.mile_label = ttk.Label(master=self.frm_entry, text="Mile")
        self.convert_button = ttk.Button(master=master,
            text="\N{RIGHTWARDS BLACK ARROW}",
            command=self.mile_to_km
        )
        self.result_label = ttk.Label(master=master, text="KM")

        # Layout the Mile Entry and Label in frm_entry using the .grid() geometry manager
        self.mile_entry.grid(row=0, column=0, sticky="e")
        self.mile_label.grid(row=0, column=1, sticky="w")

        # Set up the layout using the.grid() geometry manager
        self.frm_entry.grid(row=0, column=0, padx=10)
        self.convert_button.grid(row=0, column=1, pady=10)
        self.result_label.grid(row=0, column=2, padx=10)

    def mile_to_km(self):
        """Convert the value for Mile to KM and insert the result into lbl_result."""
        mile = self.mile_entry.get()
        km = float(mile) * 1.609344
        self.result_label["text"] = f"{round(km, 2)} KM"



def main():
    main_window = Tk()
    pomodoro = Length(main_window)
    main_window.mainloop()


if __name__ == "__main__":
    main()