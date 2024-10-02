# ages = [10, 12, 6, 18, 24, 35]


# def cust_func(x):
#     if x >= 18:
#         return True
#     else:
#         return False


# adults = list(filter(lambda x x>=1, ages))
# print(ages)
# print(adults)

# nums = list(range(1, 31))
# print(nums)
# even = list(filter(lambda x: x % 2 == 0, nums))
# odd = list(filter(lambda x: x % 2 != 0, nums))
# print(even)
# print(odd)

# names = ['Kayn', 'Renad', 'Edy', 'Stefan', 'Jack' ]
# print(names)

# short_names = list(filter(lambda x: len(x)<5, names))
# print(short_names)


# names = ['Kayn', 'Renad', 'Edy', 'Stefan', 'Jack' ]
# print(names)

# def len_name(a):
#     return len(a)


# new_list = list(map(lambda x; len(x), names))
# print(new_list)

# nums = list(range(1,11))
# print(nums)
# square_nums = list(map(lambda x: x%2==0, nums))
# print(even)

wc_teams = [('Brazil', 21), ('Germany, 19'), ('Argentina', 17)]
print(wc_teams)
new = list(map(lambda team: (team[0], team[1]+1), wc_teams))
print(new)
               
