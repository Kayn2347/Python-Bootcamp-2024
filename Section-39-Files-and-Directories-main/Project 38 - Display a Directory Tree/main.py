import pathlib


def display_tree():
    directory = pathlib.Path.cwd()
    print(f"+ {directory}")
    entries = sorted(directory.rglob("*"))
    for entry in entries:
        depth = len(entry.relative_to(directory).parts)
        spacer = '    ' * depth
        print(f"{spacer}+ {entry.name}")


display_tree()
