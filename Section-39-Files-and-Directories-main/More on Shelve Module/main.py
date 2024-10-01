import shelve


non_alcholic_drinks = ['Coke', 'Juice', 'Water', 'Tea']
alcholic_drinks = ['Beer', 'Wine', 'Vodka']
vegetables = ['onion', 'garlic', 'cucumber']
fruits = ['apple', 'orange', 'banana', 'grape']

with shelve.open('food', writeback=True) as food_file:
    # food_file['non_alcoholic_drinks'] non_alcholic_drinks
    # food_file['alcoholic_drinks'] = alcoholic_drinks
    food_file['vegetables'].append('Brocoli')
    food_file['fruits'].append('Avocado')

# Sync method
# with shelve.open('food', writeback=True) as food_file:
#    food_file['fruits'] = fruits
#    food_file.sync()
#    fruits.append('Avocado')


for food in food_file:
     print(food, food_file[food])



