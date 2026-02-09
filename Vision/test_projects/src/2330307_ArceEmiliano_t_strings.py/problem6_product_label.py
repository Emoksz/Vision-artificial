# Problem 6: Product label formatter
# Description:
# Generates a fixed-width product label of exactly 30 characters.
#
# Inputs:
# - product_name (string)
# - price_value (number)
#
# Outputs:
# - Label (30 characters)
#
# Validation:
# - Product name not empty
# - Price must be positive
#
# Test cases:
# 1) Normal: Laptop, 12500
# 2) Edge: Pen, 1
# 3) Error: "", -5

product_name = input("Enter product name: ").strip()
price_text = input("Enter price: ").strip()

try:
    price_value = float(price_text)
    if not product_name or price_value <= 0:
        raise ValueError

    label_base = f"Product: {product_name} | Price: ${price_value}"
    if len(label_base) > 30:
        label = label_base[:30]
    else:
        label = label_base + " " * (30 - len(label_base))

    print(f'Label: "{label}"')
except ValueError:
    print("Error: invalid input")
