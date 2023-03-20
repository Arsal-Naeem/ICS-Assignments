# take voltage and current readings as input from user
voltage = float(input("Enter voltage reading (in volts): "))
current = float(input("Enter current reading (in amperes): "))

# calculate wattage using formula W = V * I
wattage = voltage * current

# print wattage to the console
print(f"The wattage is: {wattage} watts")