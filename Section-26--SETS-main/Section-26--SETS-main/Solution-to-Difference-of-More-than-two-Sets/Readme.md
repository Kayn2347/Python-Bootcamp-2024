a = {1, 2, 3, 40, 50, 300, 400}
b = {10, 20, 30, 40, 300}
c = {100, 200, 300, 400}

# dif_a_b = a.difference(b)
# dif_a_b_c = dif_a_b.difference(c)
# print(dif_a_b)
# print(dif_a_b_c)

dif_a_b_c = a.difference(b, c)
print(dif_a_b_c)

print(c-b-a)