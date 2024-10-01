import os

path = os.path.join("folder1", "folder2", "folder3", "logo.png")
print(path)

print(os.getcwd())

abs_path = os.path.abspath("main.py")
print(abs_path)

abs_path = os.path.abspath("../")
print(abs_path)

# relative paths
rel_path = os.path.relpath("/Users/elshad/Desktop/Python For Everyone/Projects/OS Path Module/main.py", "Users/elshad")
print(rel_path)

rel_path = os.path.relpath("/Users/elshad/Desktop/Python For Everyone/Projects/OS Path Module/main.py", "OS Path Module/main.py")
print(rel_path)

directory_name = os.path.dirname("/Users/elshad/Desktop/Python For Everyone/Projects/OS Path Module/main.py")
print(directory_name)

file_name = os.path.basename("/Users/elshad/Desktop/Python For Everyone/Projects/OS Path Module/main.py")
print(file_name)

print(os.path.exists("/Users/elshad/Desktop/Python For Everyone/Projects/OS Path Module/main.py"))

print(os.path.isfile("/Users/elshad/Desktop/Python For Everyone/Projects/OS Path Module/main.py"))

print(os.path.isdir("/Users/elshad/Desktop/Python For Everyone/Projects/OS Path Module"))

print(os.path.getsize("/Users/elshad/Desktop/Python For Everyone/Projects/OS Path Module"))