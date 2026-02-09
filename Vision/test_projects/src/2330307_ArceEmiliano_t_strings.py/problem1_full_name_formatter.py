# Problem 1: Full name formatter (name + initials)
# Description:
# This program normalizes a full name and displays it in Title Case
# along with the person's initials.
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - Formatted name
# - Initials
#
# Validation:
# - Input must not be empty
# - Must contain at least two words
#
# Test cases:
# 1) Normal: "juan carlos tovar"
# 2) Edge: "  ana lopez  "
# 3) Error: "   "

full_name = input("Enter full name: ").strip()

if not full_name:
    print("Error: invalid input")
else:
    words = full_name.split()
    if len(words) < 2:
        print("Error: invalid input")
    else:
        formatted_name = " ".join(words).title()
        initials = ""
        for w in words:
            initials += w[0].upper() + "."
        print(f"Formatted name: {formatted_name}")
        print(f"Initials: {initials}")
