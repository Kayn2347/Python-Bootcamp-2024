file = open("sample.txt")
for line in file:
    line = line.rstrip()
    if line.startswith("Entering"):
        print(line.removeprefix("Entering with"))
