def number_of_characters(file_path):
    with open(file_path) as file:
        for index, row in enumerate(file):
            print(f"Line:{index+1} - {len(row)} characters")

number_of_occurences("pythonwiki.txt")