def count_character(word):
    output_dict = dict()
    for character in word:
        if character not in output_dict:
            output_dict[character] = 1
        else:
            output_dict[character] = output_dict[character] + 1
    return output_dict

print(count_character("BABACDAAAAS"))