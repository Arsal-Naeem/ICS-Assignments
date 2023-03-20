# Prompt the user for a number between 1-3
percentage = float(input("Enter your Percentage: "))

# Calculate the grade based on the percentage and print it
if percentage >= 100:
    print("Invalid input")
elif percentage >= 90:
    print("A+")
elif percentage >= 80:
    print("A")
elif percentage >= 70:
    print("B+")
elif percentage >= 60:
    print("B")
elif percentage >= 50:
    print("C")
elif percentage >= 40:
    print("D")
else:
    print("F")