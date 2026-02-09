# Problem 3: Product catalog with dictionary

product_prices = {
    "apple": 10.0,
    "banana": 5.0,
    "orange": 8.0
}

product_name = "apple".strip().lower()
quantity = 3

if quantity > 0 and product_name in product_prices:
    unit_price = product_prices[product_name]
    total_price = unit_price * quantity
    print("Unit price:", unit_price)
    print("Quantity:", quantity)
    print("Total:", total_price)
else:
    print("Error: product not found")
