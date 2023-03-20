# Prompt the user to enter (x,y) coordinates of the point
x, y = input("Enter (x,y) coordinates of the point: ").split(",")

# Calculate the distance of the point from the origin
distance = (float(x)**2 + float(y)**2) ** 0.5

# Check if the distance is greater than the radius of the circle
if distance > 10:
    print("Outside the circle")
else:
    print("Inside the circle")