# Program that displays the price of bread bought by a customer, the discount
# if the customer has bought day-old bread, then the total price, with all
# values displayed to two decimal places .

# Discount factor
discount = 0.4 # factor
bread_cost = 3.49

# User input prompt
new_bread = int(input("Loaves of fresh bread: "))
old_bread = int(input("Loaves of day old bread: "))

# Calculating the regualr price, price after discount and the savings made by
# customer
reg_price = (new_bread + old_bread) * bread_cost
dis_price = bread_cost * (new_bread + old_bread * discount)
savings = reg_price - dis_price

print("Regular price: $%.2f \nAfter discount: $%.2f \nYour savings today: $%.2f"\
 % (reg_price, dis_price, savings))
