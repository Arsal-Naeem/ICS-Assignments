# Taking input from the user for the original selling price and discount percentage
original_price = float(input("Enter the original selling price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculating the discounted selling price
discount = (discount_percent / 100) * original_price
discounted_price = original_price - discount

# Printing the discounted selling price with two decimal places
print(f"Discounted Selling Price: {format(discounted_price, '.2f')}")