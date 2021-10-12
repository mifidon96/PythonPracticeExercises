# Program that generates a table of original prices and discounted amounts. #

# Setting up the multiplier to get the discounted final price, and the dicount
# itself
discounted_multi = 0.4
discount_multi = 1 - discounted_multi
# Setting original prices
prices = [4.95, 9.95, 14.95, 19.95, 24.95]
# calculating the new price and the amount saved
for i in prices:
    new_price = i * discounted_multi
    amount_saved = i * discount_multi
    print("Original price: $%.2f \nDiscount amount: $%.2f \nNew price: $%.2f\n" \
    % (i, amount_saved, new_price))
