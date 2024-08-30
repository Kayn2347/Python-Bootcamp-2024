list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200] 

def numbers_divisible_byfive(p_list):
    for item in p_list:
        if item > 130:
            break
        if (item % 5 == 0):
            print(item)
    print("STOP")

numbers_divisible_byfive(list1)