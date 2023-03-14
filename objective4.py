# Prompt the user for the total marks
total_marks = float(input("Enter total marks: "))

# Initialize an empty list to store the marks
marks = []

# Use a for loop to prompt the user for the marks of each subject and append them to the list
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

# Calculate the total obtained marks
obtained_marks = sum(marks)

# Check if the obtained marks are greater than the total marks
if obtained_marks > total_marks:
    print("The Total marks cannot be less than the obtained marks.")
elif total_marks <= 0:
    print("The Total marks should be greater than zero")
else:
    # Calculate the percentage
    percentage = (obtained_marks / total_marks) * 100

    # Print the total obtained marks and percentage
    print(f"Total obtained marks: {obtained_marks}")
    print(f"Percentage: {percentage:.2f}%")