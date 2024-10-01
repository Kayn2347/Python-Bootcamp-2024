from datetime import datetime
import pathlib


directory = pathlib.Path.cwd()


def find_last_modified(directory):
    time = 0
    file = pathlib.Path(".")
    for f in directory.iterdir():
        if time < f.stat().st_mtime:
            time = f.stat().st_mtime
            file = f.name
    return f"Date modified: {datetime.fromtimestamp(time)}, Filename: {file}"


print(find_last_modified(directory))
