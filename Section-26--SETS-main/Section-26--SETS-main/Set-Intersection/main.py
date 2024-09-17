fruits = {"apple", "orange", "cucumber", "grape", "pear", "limon"}
vegetables = {"cucumber", "onion", "garlic", "pepper", "broccoli"}
mixed = {"cucumber", "onion", "apple"}

set1 = set(range(20))
set2 = set(range(0,20,2))
set3 = set(range(0,20,3))
print(set1)
print(set2)
print(set3)

print(set.intersection(set1, set2, set3))