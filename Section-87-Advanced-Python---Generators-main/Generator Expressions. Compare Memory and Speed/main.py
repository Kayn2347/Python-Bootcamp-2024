import sys
import cProfile

# square = (num**2 for num in range(1, 11))
# print(list(square))
# print(set(square))

square_ge = (num**2 for num in range(1, 5000))
square_lc = [num**2 for num in range(1, 5000)]

print(cProfile.run("max((num**2 for num in range(1, 5000)))"))
print(cProfile.run("max([num**2 for num in range(1, 5000)]"))
