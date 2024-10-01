import shelve


non_alcoholic_drinks = ['Coke', 'Juice', 'Water', 'Tea']
alcoholic_drinks = ['Beer', 'Wine', 'Vodka']
vegetables = ['onion', 'garlic', 'cucumber']
fruits = ['apple', 'orange', 'banana', 'grape']

with shelve.open('food', writeback=True) as food_file:
    food_file['fruits'] = fruits
    food_file.sync()
    fruits.append('Avocado')

    for food in food_file:
        print(food, food_file[food])

