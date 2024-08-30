list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']
list2 = ['cbc', 'xyz', 'aba', '2332', 'abc', 'ab', 'aa', 'trt']

def count_words(p_list):
    ctr = 0
    for word in p_list:
        if len(word) >= 2 and word[0] == word[-1]:
            ctr += 1
    return ctr

print(count_words(list2))