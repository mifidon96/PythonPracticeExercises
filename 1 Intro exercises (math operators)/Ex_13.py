# cash register program that determines the amount of change to be givern to a 
# customer in canadian coins

# input in cents
cents = int(input("Amount charged to customer in cents:"))

# number of toonies
toonie = cents//200
remain = cents - (toonie*200)

loonie = remain//100
remain -= quarter * 25

dime = remain//10
remain -= dime * 10

nickel = remain//5
remain -= dime * 10

nickel = remain//5
remain -= nickel * 5

penny = remain//1

print("Toonies: %s \n" % toonie)
print("LoonieS: %s \n" % loonie)
print("Quarters: %s \n" % quarter)
print("Dimes: %s \n" % dime)
print("Nickels: %s \n" % nickel)
print("Pennies: %s \n" % penny)
