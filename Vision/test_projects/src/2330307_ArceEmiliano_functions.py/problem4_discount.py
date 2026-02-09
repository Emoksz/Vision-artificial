def apply_discount(prices, discount):
    return [p * (1 - discount) for p in prices]

prices_text = "100,200,300"
discount = 0.10
prices = []

valid = True
for p in prices_text.split(","):
    try:
        value = float(p)
        if value <= 0:
            valid = False
        prices.append(value)
    except ValueError:
        valid = False

if valid and 0 <= discount <= 1:
    print("Original:", prices)
    print("Discounted:", apply_discount(prices, discount))
else:
    print("Error: invalid input")
