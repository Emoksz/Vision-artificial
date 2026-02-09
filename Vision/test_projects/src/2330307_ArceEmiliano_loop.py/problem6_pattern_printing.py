# Problem 6: Pattern printing with nested loops
# Description:
# Prints a right triangle pattern using asterisks.

# Inputs:
# - n (int)

# Outputs:
# - Asterisk pattern

# Validations:
# - n must be integer
# - n >= 1

# Test cases:
# 1) Normal: n=4
# 2) Edge: n=1
# 3) Error: n=0

try:
    n = int(input("Enter number of rows: "))

    if n < 1:
        print("Error: invalid input")
    else:
        for i in range(1, n + 1):
            line = ""
            for j in range(i):
                line += "*"
            print(line)

except ValueError:
    print("Error: invalid input")
