import random

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


# Step 3 - Create Question Files and randomize the questions
# - TODO 3.1 - Generate questions files based on number of students

# - TODO 3.4 - Loop through number of questions and make a question 				for each
for quiz_num in range(student_count):
   # Create quiz file
   with open(f'questions{quiz_num+1}.txt', 'w') as quiz_file:
       # - TODO 3.2 - Write header for the quiz in questions text files
      quiz_file.write('Name: \n\nDate:\n\n')
      quiz_file.write(f"{' ' * 20} Country Capital Quiz (Form {quiz_num+1})")
      quiz_file.write('\n\n')
      # - TODO 3.3 - Shuffle the order of countries based on random module
      country_list = list(countries.keys())
      random.shuffle(country_list)
      # - TODO 3.4 - Loop through number of questions and make a question 				for each
      for question_num in range(question_count):
      