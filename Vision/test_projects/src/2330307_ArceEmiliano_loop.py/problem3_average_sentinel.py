# Problem 3: Average of numbers with sentinel
# Description:
# Reads numbers until a sentinel value is entered and calculates the average.

# Inputs:
# - numbers (float)
# - sentinel value = -1

# Outputs:
# - Count
# - Average

# Validations:
# - Input must be numeric
# - Only values >= 0 are accepted

# Test cases:
# 1) Normal: 4, 6, 8, -1
# 2) Edge: -1
# 3) Error: text input

SENTINEL_VALUE = -1

count = 0
total_sum = 0.0

while True:
    user_input = input("Enter a number (-1 to finish): ")

    try:
        number = float(user_input)
    except ValueError:
        print("Error: invalid input")
        continue

    if number == SENTINEL_VALUE:
        break

    if number < 0:
        print("Error: invalid input")
        continue

    count += 1
    total_sum += number

if count == 0:
    print("Error: no data")
else:
    average = total_sum / count
    print("Count:", count)
    print("Average:", average)
