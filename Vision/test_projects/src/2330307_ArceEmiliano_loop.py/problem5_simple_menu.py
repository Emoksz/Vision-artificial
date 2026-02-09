# Problem 5: Simple menu with while
# Description:
# Displays a menu that repeats until the user exits.

# Inputs:
# - option (int)

# Outputs:
# - Menu actions

# Validations:
# - Only options 0,1,2,3 are valid

# Test cases:
# 1) Normal: option 1
# 2) Edge: option 0
# 3) Error: invalid option

counter = 0
option = -1

while option != 0:
    print("\n1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    try:
        option = int(input("Select an option: "))
    except ValueError:
        print("Error: invalid option")
        continue

    if option == 1:
        print("Hello!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter += 1
        print("Counter incremented")
    elif option == 0:
        print("Bye!")
    else:
        print("Error: invalid option")
