# Step 1 - Create sentence maker function
# Step 2 - Create a loop which ask input from a user Continously
# Step 3 - Combine everything together

def sentence_maker(text):
    question_words = ['what', 'how', 'why']
    capitalized_text = text.capitalize()
    for word in question_words:
        if text.startswith(word):
           return "{}.".format(capitalized_text)
    return"{}".format(capitalized_text)

result =[]
while True:
    user_input = input("what is on your mind?")
    if user_input == "\end":
        break
    else:
        complete_sentence = sentence_maker(user_input)
        result.append(complete_sentence)

story = " ".join(result)
print(story)