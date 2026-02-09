# Problem 1: Shopping list basics (list operations)
# Description:
# This program works with a shopping list stored as a list.
# Each item includes the product name and its quantity.
# It allows adding a new product, counting items,
# and checking if a product exists in the list.

# Inputs
initial_items_text = "apple:2, banana:5, orange:6"
new_item = "grape:4"
search_item = "banana"

# Validations
if not initial_items_text.strip() or not new_item.strip() or not search_item.strip():
    print("Error: invalid input")
else:
    # Process initial list
    items_list = []
    raw_items = initial_items_text.split(",")

    for item in raw_items:
        cleaned_item = item.strip().lower()
        items_list.append(cleaned_item)

    # Normalize and add new item
    items_list.append(new_item.strip().lower())

    # Search product (only by name, not quantity)
    is_in_list = False
    for item in items_list:
        product_name = item.split(":")[0]
        if product_name == search_item.strip().lower():
            is_in_list = True
            break

    # Outputs
    print("Items list:", items_list)
    print("Total items:", len(items_list))
    print("Found item:", is_in_list)
