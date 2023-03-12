from math import pi

# Taking input from the user for the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculating the circumference and area of the circle
circumference = 2 * pi * radius
area = pi * radius * radius

# Printing the circumference and area with two decimal places
print(f"Circumference: {format(circumference, '.2f')}")
print(f"Area: {round(area, 2)}")