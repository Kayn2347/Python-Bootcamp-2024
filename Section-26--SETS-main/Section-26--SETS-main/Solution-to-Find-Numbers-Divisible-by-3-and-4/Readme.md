
def divisible_by_3and4(n):
    set1 = set(range(0,100,3))
    set2 = set(range(0,100,4))
    set3 = set1.intersection(set2)
    return set3

