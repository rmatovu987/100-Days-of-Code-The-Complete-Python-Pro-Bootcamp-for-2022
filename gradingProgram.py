#!/usr/bin/env python3
"""Create a grading program"""

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

# create empty dictionary of grades
student_grades = {}

# grade the students based on their scores
for student in student_scores:
    score = student_scores[student]
    if score < 71:
        student_grades[student] = "Fail"
    elif score < 81:
        student_grades[student] = "Acceptable"
    elif score < 91:
        student_grades[student] = "Exceeds Expectation"
    else:
        student_grades[student] = "Outstanding"

print(student_grades)
