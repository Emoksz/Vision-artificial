def summarize_numbers(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

numbers_text = "100,400,500"
numbers = []

valid = True
for n in numbers_text.split(","):
    try:
        numbers.append(float(n))
    except ValueError:
        valid = False

if valid and numbers:
    mn, mx, avg = summarize_numbers(numbers)
    print("Min:", mn)
    print("Max:", mx)
    print("Average:", avg)
else:
    print("Error: invalid input")
