discounted_price = float(input("Enter the discounted selling price: "))
discount_percentage = float(input("Enter the discount percentage: "))

if discount_percentage < 100:
    original_price = discounted_price / (1 - (discount_percentage / 100))
    print(f"The original selling price is: ${format(original_price, '.2f')}")
else:
    print("Discount can only be less than 100%")