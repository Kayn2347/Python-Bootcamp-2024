names = ['Kayn', 'Renad', 'Edy', 'Stefan', 'Jack' ]


def contains_n(p_names):
    for name in p_names:
        if 'n' in name:
            yield name


gen_ob = contains_n(names)
# print(list)(gen_ob))
# print(set)(contains_n(names)))
# print(tuple(gen_ob))

for element in gen_ob:
  print(element)

print(list(gen_ob))
print(list(gen_ob))
print(list(gen_ob))
print(list(gen_ob))
