def number_of_lines():
    file_name = input('Enter the file name: ')
    try:
        file = open(file_name)
    except:
        print('File cannot be opened:', file_name)
        exit()
    word = input("Enter the word: ")
    count = 0
    for line in file:
        if line.startswith(word):
            count = count + 1
    print(f'There are {count} {word} lines in {file_name}')


number_of_lines()
