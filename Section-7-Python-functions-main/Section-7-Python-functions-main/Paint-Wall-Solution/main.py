import math

def calculate_can_number(height, width, coverage):
    area = height * width
    number_of_cans = math.ceil(area / coverage)
    print(number_of_cans)


height = int(input("Enter height of wall: "))
width = int(input("Enter width of wall: "))

calculate_can_number(height,width,4)
