student_scores = {
  "Chisee": 90,
  "Kayn": 68,
  "Zion": 88, 
  "Dhea": 79,
  "Heart": 62,
}

def convert_grade(p_dict):
    student_grades = {}
    for key in p_dict:
        score = p_dict[key]
        if score >= 85:
            student_grades[key] = "Outstanding"
        elif score >= 65:
            student_grades[key] = "Good"
        elif score >= 50:
            student_grades[key] = "Acceptable"
        else:
           student_grades[key] = "Fail" 
    return student_grades


print(convert_grade(student_scores))