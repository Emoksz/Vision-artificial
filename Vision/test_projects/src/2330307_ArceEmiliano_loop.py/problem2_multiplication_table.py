# Problem 2: Multiplication table with for
# Description:
# This program prints the multiplication table of a base number.

# Inputs:
# - base (int)
# - m (int)

# Outputs:
# - base x i = result

# Validations:
# - base and m must be integers
# - m >= 1

# Test cases:
# 1) Normal: base=5, m=4
# 2) Edge: base=3, m=1
# 3) Error: m=0

try:
    base = int(input("Enter base number: "))
    m = int(input("Enter limit m: "))

    if m < 1:
        print("Error: invalid input")
    else:
        for i in range(1, m + 1):
            print(f"{base} x {i} = {base * i}")

except ValueError:
    print("Error: invalid input")
