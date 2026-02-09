# Problem 4: Student grades with dict and list

students_grades = {
    "Alice": [85.0, 90.0, 88.0],
    "Bob": [60.0, 70.0, 65.0],
    "Charlie": [100.0, 95.0]
}

student_name = "Bob".strip().title()

if student_name in students_grades and students_grades[student_name]:
    grades_list = students_grades[student_name]
    average = sum(grades_list) / len(grades_list)
    is_passed = average >= 70.0
    print("Grades:", grades_list)
    print("Average:", round(average, 2))
    print("Passed:", is_passed)
else:
    print("Error: student not found")
