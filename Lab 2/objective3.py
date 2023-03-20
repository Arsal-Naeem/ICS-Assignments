# Prompt the user for a number between 1-3
num = int(input("Input any number between 1-3: "))

# Compare the user's input with 1, 2 and 3 and give output accordingly
if num == 1:
    print("Thank You")
elif num == 2:
    print("Well Done")
elif num == 3:
    print("Correct")
else:
    print("Error: You can only input num between 1-3")