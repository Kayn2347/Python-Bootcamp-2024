#Step 1 - Prompt for question and student numbers
#TODO 1.1 - Ask from user the number of questions and the number of 				students in class
question_count = int(input("How many questions will be for each quiz?"))
student_count = int(input("How many students will participate in quiz?"))
# Step 2 - Parse country data text file in a Dictionary
# - TODO 2.1 - Create empty countries dictionary
countries = {}
# - TODO 2.2 - Open country_data.txt file
# - TODO 2.3 - Parse data in countries dictionary
with open('country_data.txt') as country_info:
   country_info.readline()
   for country in country_info:
       info_list = country.strip().split(";")
       name, capital = info_list[1:3]
       countries[name] = capital

print(countries)