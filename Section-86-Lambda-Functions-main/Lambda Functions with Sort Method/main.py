# my_list = [2, 5, 3, 5, 9, 6, ,3]
# my_list.sort()
# print(my_list)

# names =['Evan Park', 'Edy Lucky', 'Kelly Adams', 'Smith Baker']
# print(names)
# name.sort(key=lambda x: x.split()[1])
# print(names)

# people = [('Evan', 20), ('Edy', 19), ('Kelly', 30), ('Smith', 25)]
# people.sort(key=lambda x: x[1])
# print(people)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name}:{self.age}'


evan = Person('Evan', 20)
edy = Person('Edy', 19)
kelly = Person('Kelly', 30)
smith = Person('Smith', 25)

persons = [evan, edy, kelly]
print(persons)
persons.sort(key=lambda x: x.name)
print(persons)

