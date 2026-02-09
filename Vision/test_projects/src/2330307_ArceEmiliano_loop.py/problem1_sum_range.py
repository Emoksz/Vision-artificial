# Problem 1: Sum of integers in a range
# Description:
# This program calculates the sum of all integers from 1 to n.
# It also calculates the sum of only the even numbers in that range.

# Inputs:
# - n (int)

# Outputs:
# - Sum 1..n
# - Even sum 1..n

# Validations:
# - n must be an integer
# - n >= 1

# Test cases:
# 1) Normal: n = 5 → Sum = 15, Even sum = 6
# 2) Edge: n = 1 → Sum = 1, Even sum = 0
# 3) Error: n = -3 → Error

try:
    n = int(input("Enter n: "))
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for i in range(1, n + 1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)

except ValueError:
    print("Error: invalid input")
