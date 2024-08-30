student_scores = [80, 60, 50, 65, 75, 55]

def sum_score_above_average(p_student_scores):
    sum_score = 0
    number_of_students = 0
    for score in p_student_scores:
        sum_score += score
        number_of_students += 1
    average_score = sum_score / number_of_students
    sum_above_average = 0
    for score in p_student_scores:
        if score > average_score:
            sum_above_average += score
            print(average_score, score)
    return sum_above_average

print(sum_score_above_average(student_scores))