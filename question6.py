# take the lengths of the parallel sides and the perpendicular distance as input from user
a = float(input("Enter the length of the first parallel side: "))
b = float(input("Enter the length of the second parallel side: "))
h = float(input("Enter the perpendicular distance between the two parallel sides: "))

# Calculate the area of the trapezoid
area = ((a + b) / 2) * h

# Print the area of the trapezoid
print(f"The area of the trapezoid is {format(area, '.2f')}")