# Prompt the user to input a number between 10 and 20 (inclusive)
num = int(input("Enter a number between 10 and 20(inclusive): "))

# Check if the number is within the specified range
if num <= 20 and num >= 10:
    # If the number is within the range, print "Thank you"
    print("Thank you")
else:
    # If the number is not within the range, print "Incorrect answer"
    print("Incorrect answer")