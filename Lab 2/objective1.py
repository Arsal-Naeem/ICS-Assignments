# Prompt the user for a number between 10-20(inclusive)
num = int(input("Enter a number between 10 and 20(inclusive): "))

# Check if the num lies between 10-20
if num <= 20 and num >= 10:
    print("Thank you")
else:
    print("Incorrect answer")