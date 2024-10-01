with open("timetable.txt", 'a') as file:
    for i in range(2, 21):
        for j in range(1, 21):
            print(f"{i} times {j} = {i*j}", file=tt_file)
        print("-" * 18, file=tt_file)
