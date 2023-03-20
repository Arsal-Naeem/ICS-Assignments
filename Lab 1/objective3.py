# Prompt the user for the number of days and store it in a variable
days = int(input("Enter the number of days: "))

# Calculate the number of hours, minutes, and seconds from the number of days
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# Print the results
print(f"{days} days = {hours} hours = {minutes} minutes = {seconds} seconds")