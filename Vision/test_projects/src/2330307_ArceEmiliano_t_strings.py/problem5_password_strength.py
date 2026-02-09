# Problem 5: Password strength classifier
# Description:
# Classifies a password as weak, medium, or strong.
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - Password strength
#
# Validation:
# - Must not be empty
#
# Test cases:
# 1) Normal: Abc123!
# 2) Edge: password123
# 3) Error: ""

password_input = input("Enter password: ")

if not password_input:
    print("Error: invalid input")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for ch in password_input:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isalnum():
            has_symbol = True

    if len(password_input) < 8:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "medium"

    print(f"Password strength: {strength}")
