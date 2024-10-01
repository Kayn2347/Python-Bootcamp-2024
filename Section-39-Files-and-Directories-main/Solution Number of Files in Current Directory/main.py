import os

entries = os.scandir(".")
total = 0
for entry in entries:
    if entry.is_file():
        total += 1

print(total)
