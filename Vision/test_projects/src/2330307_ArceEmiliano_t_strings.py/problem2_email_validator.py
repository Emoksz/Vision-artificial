# Problem 2: Simple email validator
# Description:
# Validates a basic email structure and extracts the domain.
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - Valid email: True / False
# - Domain (if valid)
#
# Validation:
# - Must not be empty
# - Exactly one '@'
# - No spaces
# - Domain must contain '.'
#
# Test cases:
# 1) Normal: user@mail.com
# 2) Edge: a@b.c
# 3) Error: user mail.com

email_text = input("Enter email: ").strip()

valid = True

if not email_text:
    valid = False
elif email_text.count("@") != 1:
    valid = False
elif " " in email_text:
    valid = False
else:
    at_pos = email_text.find("@")
    domain = email_text[at_pos + 1:]
    if "." not in domain:
        valid = False

print(f"Valid email: {valid}")
if valid:
    print(f"Domain: {domain}")
