# Taking input from the user for obtained marks and maximum marks
obtained_marks = int(input("Enter obtained marks: "))
max_marks = int(input("Enter maximum marks: "))

# Using try-except block to handle divide-by-zero error
try:
    # Calculating the percentage and printing it
    percentage = (obtained_marks / max_marks) * 100
    print(f"Percentage: {format(percentage, '.2f')}%")
except ZeroDivisionError:
    print("Maximum marks can not be 0")