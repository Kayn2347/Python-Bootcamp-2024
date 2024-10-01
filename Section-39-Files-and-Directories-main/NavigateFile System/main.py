import os


def display_cwd():
    cwd = os.getcwd()
    print(f"Current working directory: {cwd}")


def up_one_directory_level():
    os.chdir("../")


def display_entries_in_directory(directory):
    entries = os.scandir(directory)
    for entry in entries:
        print(entry.name)


display_cwd()
up_one_directory_level()
up_one_directory_level()
display_cwd()
display_entries_in_directory("Desktop/Python For Everyone/Lectures")