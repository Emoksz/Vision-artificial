def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = 90

if 0 <= score <= 100:
    print("Score:", score)
    print("Category:", classify_grade(score))
else:
    print("Error: invalid input")
