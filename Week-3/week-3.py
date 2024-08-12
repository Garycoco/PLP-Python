"""
    1. Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
        The function should take the original price (price) and the discount percentage (discount_percent) as parameters.
        If the discount is 20% or higher, apply the discount; otherwise, return the original price.

    2. Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
        Print the final price after applying the discount, or if no discount was applied, print the original price.
"""

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