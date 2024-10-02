from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


class TextEditor:
    def __init__(self, master):
        self.master = master
        master.title("Simple Text Editor")

        master.rowconfigure(0, minsize=800, weight=1)
        master.columnconfigure(1, minsize=800, weight=1)

        self.text_editor = Text(master)
        self.button_frame = Frame(master, relief=RAISED, bd=2)
        self.open_button = Button(self.button_frame, text="Open", command=self.file_open)
        self.save_button = Button(self.button_frame, text="Save As...", command=self.save_file)

        self.open_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.save_button.grid(row=1, column=0, sticky="ew", padx=5)

        self.button_frame.grid(row=0, column=0, sticky="ns")
        self.text_editor.grid(row=0, column=1, sticky="nsew")

    def file_open(self):
        """Open a file for in text editor for editting."""
        file_path = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not file_path:
            return
        self.text_editor.delete("1.0", END)
        with open(file_path, mode="r", encoding="utf-8") as input_file:
            text = input_file.read()
            self.text_editor.insert(END, text)
        self.master.title(f"Simple Text Editor - {file_path}")

    def save_file(self):
        """Save the current file as a new file in txt format."""
        file_path = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not file_path:
            return
        with open(file_path, mode="w", encoding="utf-8") as output_file:
            text = self.text_editor.get("1.0", END)
            output_file.write(text)
        self.master.title(f"Simple Text Editor - {file_path}")


def main():
    main_window = Tk()
    text_editor = TextEditor(main_window)
    main_window.mainloop()


if __name__ == "__main__":
    main()
