# Prompt the user for x and y coordinates of the point
x,y = input("Enter (x,y) coordinates of the points: ").split(",")

# Using formula: x²+y²=r² to check if the point lies within the circle
if float(x)**2 + float(y)**2 > 10**2:
    print("Outside the Circle")
else:
    print("Inside the circle")