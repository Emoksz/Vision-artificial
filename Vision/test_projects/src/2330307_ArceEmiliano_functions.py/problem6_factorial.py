def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 5

if isinstance(n, int) and 0 <= n <= 20:
    print("Factorial:", factorial(n))
else:
    print("Error: invalid input")
