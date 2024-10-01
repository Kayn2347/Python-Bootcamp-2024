import pathlib import Path 


def display_directory_content():
    entries = Path.cwd()
    for entry in entries.iterdir():
        print(f"File name: {entry.name}")
        print(f"File folder: {entry.parent}")
        print(f"File name wt ex:{entry.stem}")
        print(f"File ex: {entry.suffix}")
        print()


display_directory_content()
