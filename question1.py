# Taking input from the user for obtained marks and total marks
obtained_marks = int(input("Enter obtained marks: "))
total_marks = int(input("Enter total marks: "))

# Check if the obtained marks are greater than the total marks
if obtained_marks <= total_marks and total_marks != 0:
    # Calculating the percentage and printing it
    percentage = (obtained_marks / total_marks) * 100
    print(f"Percentage: {format(percentage, '.2f')}%")
else:
    print("The Total marks should be greater than zero and cannot be less than the obtained marks.")