# Prompt the user for the basic salary
basic_salary = float(input("Enter the basic salary: "))

# Calculate the HRA and DA based on the basic salary
if basic_salary < 1500:
    hra = 0.1 * basic_salary
    da = 0.9 * basic_salary
else:
    hra = 500
    da = 0.98 * basic_salary

# Calculate the gross salary
gross_salary = basic_salary + hra + da

# Print the gross salary
print(f"Gross salary: {gross_salary}")