# Prompt user for their name and age, and store them in variables called name and age.
name = input("Your Name: ")
age = int(input("Your age: "))

# Increment the user's age to calculate their age at their next birthday.
age += 1 

# Print a message that includes the user's name and calculated age.
print(f"{name}, next birthday you will be {age}")