# Problem 3: Discount eligibility with booleans

try:
    purchase_total = float(input("Enter purchase total: "))
    is_student_text = input("Is student (YES/NO): ").strip().upper()
    is_senior_text = input("Is senior (YES/NO): ").strip().upper()

    if purchase_total < 0 or is_student_text not in ["YES", "NO"] or is_senior_text not in ["YES", "NO"]:
        print("Error: invalid input")
    else:
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"

        discount_eligible = is_student or is_senior or purchase_total >= 1000.0
        final_total = purchase_total * 0.9 if discount_eligible else purchase_total

        print("Discount eligible:", discount_eligible)
        print("Final total:", final_total)

except ValueError:
    print("Error: invalid input")
