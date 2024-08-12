def calculate_discount(price: float, discount_percent: float):
    if (discount_percent >= 20):
        discount = discount_percent / 100
        discount_amount = price - (price * discount)
        return discount_amount
    else:
        return price
# Prompting the user to enter price and discount percent    
price = float(input("Please enter the original price: "))
discount_percent = float(input("Please enter the discount percentage: "))

# Printing a message based on whether the discount was applied or not
amount = calculate_discount(price, discount_percent)
if (discount_percent >= 20):
    print(f"Discount applied. Final price: {amount}")
else:
    print(f"Price: {amount}")