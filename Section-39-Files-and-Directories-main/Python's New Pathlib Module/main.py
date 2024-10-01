import pathlib import Path 


path = Path.cwd()
file_names = path.glob("**/*.txt")
for file_name in file_names:
    print(file_name.stem)
    print(file_name.parent)
