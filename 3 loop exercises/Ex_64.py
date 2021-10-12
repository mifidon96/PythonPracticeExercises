# Program that figures out the total cost of a list of items,
# total price and price rounded to the nearest 5 cents canadian #

print("Please enter the price of each item. Followed by a blank entry for total.")

# initializing price entry, n counter, total price
entry = 0
total = 0
n = 0
# Setting dollar to penny, penny to nickel, and nickel to dollar conversion
# factors
d_p = 0.01
p_n = 5
n_d = 0.05

while entry != "":
    n += 1
    entry = input("Cost of item %d: " % n)
    if entry != "":
        entry = float(entry)
        total += entry

# number of pennies
pennies = total / d_p
# number of whole nickels in the number of pennies
nickels = pennies // p_n
# remainder left after
remainder = pennies % p_n
# rounding up to nearest nickel
if remainder >= 2.5:
    remainder = 5
# rounding down
else:
    remainder = 0

# converting total nickels back into dollars and adding remainder
total_cash = (nickels * n_d) + (remainder * d_p)
# Displaying total amount
print("Total cost of times $%.2f \nTotal cost in cash: $%.2f" % (total, total_cash))
