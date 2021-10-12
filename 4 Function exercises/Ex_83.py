# A function that calculates an express shipping charge, taking number of
# items as its only parameter and returning only the price #

# Defining shipping price function
def ship(n):
    base = 10.95
    add_ppu = 2.95
    
    total = base + add_ppu * (n-1)
    return total

# Prompting user input
n = int(input("Please enter the number of items: "))

# Displaying output
price = ship(n)
print("The total hipping price: $%.2f" % price)
