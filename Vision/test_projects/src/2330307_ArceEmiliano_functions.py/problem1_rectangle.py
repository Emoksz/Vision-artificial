def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

width = 3
height = 2

if width > 0 and height > 0:
    print("Area:", calculate_area(width, height))
    print("Perimeter:", calculate_perimeter(width, height))
else:
    print("Error: invalid input")
