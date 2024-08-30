names = ['Kayn', 'heart', 'Chisee', 'Zion']
scores = [90, 95, 80, 75]
print("{0:<10} {1:<5}".format("Name","Score"))
for index in range(len(names)):  
    print("{0:<10} {1:<5}".format(names[index],scores[index]))