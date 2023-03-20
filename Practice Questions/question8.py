# Prompt the user to enter the lengths of the three sides of the triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

# Calculate the semiperimeter of the triangle
s = (a + b + c) / 2

# Calculate the area of the triangle using Heron's formula
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Print the area of the triangle
print(f"The area of the triangle is {format(area, '.2f')}")