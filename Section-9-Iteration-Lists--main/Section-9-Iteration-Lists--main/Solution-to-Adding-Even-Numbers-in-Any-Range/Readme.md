def odd_even_numbers(start, end):
total = 0
for number in range(start, end+1):
  if number % 2 == 0:
    total += number
return total    