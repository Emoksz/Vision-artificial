# Problem 4: Password attempts with while
# Description:
# Simple password validation system with limited attempts.

# Inputs:
# - user_password (string)

# Outputs:
# - Login success
# - Account locked

# Validations:
# - MAX_ATTEMPTS > 0

# Test cases:
# 1) Normal: correct password on first try
# 2) Edge: correct on last attempt
# 3) Error: all attempts wrong

CORRECT_PASSWORD = "emix123"
MAX_ATTEMPTS = 3

attempts = 0

while attempts < MAX_ATTEMPTS:
    user_password = input("Enter password: ")

    if user_password == CORRECT_PASSWORD:
        print("Login success")
        break
    else:
        attempts += 1

if attempts == MAX_ATTEMPTS:
    print("Account locked")
