# Problem 2: Points and distances with tuples

x1, y1, x2, y2 = 0.0, 0.0, 4.0, 3.0

point_a = (x1, y1)
point_b = (x2, y2)

distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

print("Point A:", point_a)
print("Point B:", point_b)
print("Distance:", round(distance, 2))
print("Midpoint:", midpoint)
