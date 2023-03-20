# Prompt the user for thier age
age = int(input("Enter your age: "))

#Check the user age and print activities in accordance
if age >= 18:
    print("You can vote")
elif age == 17:
    print("You can learn to drive")
elif age == 16:
    print("You can buy a lottery ticket")
else:
    print("You can go trick or treating")