# program that calculates a taxi fare. Function takes distance traveled (km) as
# its only parameter and returns total fare as the only result. #

# Setting base fare
base = 4.00

# Defining rate function (parameters: distance, returns: fare for distance traveled)
def rate(d):
    price = 0.25
    fare = (d/0.14)*price
    return fare

# Prompting user input, passing to function, calculates total, displays output
d = float(input("Enter the distance in km: "))
total = rate(d) + base
print("$%.2f" % total)
