# program that calculate the total charge for admission of a group to a zoo.
# Prices vary on age brackett #

# Initializing total to 0 and guest counter to 1
total = 0
n = 1
# setting ages of admision prices
infant = 2
child_low = 3
child_high = 12
senior = 65
# Setting admission prices
free = 0
child_price = 14.00
senior_price = 18.00
general_price = 23.00
# Prompting first input from user
age = input("Enter the age of guest %d (blank to quit): " % n)

# Setting escape condition for loop
while age != "":
    #converting string entry to integer
    age = int(age)
    # determining age brackett nd corresponding price
    if age <= infant:
        price = free
    elif child_low <= age <= child_high:
        price = child_price
    elif age >= senior:
        price = senior_price
    else:
        price = general_price
    # Incrasing gues counter by one, adding price to running total, prompting user
    # for next input / escape condition.
    n += 1
    total += price
    age = input("Enter the age of guest %d (Blank to quit): " % n)
# Displaying output.
print("Total cost for group: $%.2f" % total)
