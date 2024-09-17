fruits = {"apple", "pear", "limon", "grape", "orange"}
vegetables = {"cucumber", "garlic", "onion", "broccoli", "pepper"}

all_together1 = fruits.union(vegetables)
print(all_together1)

all_together2 = vegetables.union(fruits)
print(all_together2)

# pipe operator
all_together3 = vegetables | fruits
print(all_together3)