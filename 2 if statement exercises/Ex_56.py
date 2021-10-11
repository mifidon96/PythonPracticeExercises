# A programme that calucaltes the phone bill of a user based on the number of
# minutes and texts they have used.

# Assigning numerical data to variables.
# Included minutes and texts
mins_incl = 50
texts_incl = 50
# Flat rate costs
monthly = 15
emerg_charge = 0.44
# Extra cost multipliers
add_min = 0.25
add_text = 0.15
# tax multiplier (tax at 5%)
tax_multi = 1.05
# initializing total
total = 0

# Prompting user input
mins_used = float(input("Please enter the number of minutes used this month: "))
texts_used = float(input("Please enter the number of texts sent this month: "))

# Displaying flat rate charges and adding costs to running total
print("Monthly flat rate charge: $%.2f" % monthly)
print("911 call centre support flat rate charge: $%.2f" % emerg_charge)
total = monthly + emerg_charge

 # calculating if extra costs exist (extra minutes and/ textes) and adding them to running total
if mins_used > mins_incl:
    mins_extra = mins_used - mins_incl
    charge = mins_extra * add_min
    print("%.0f extra minutes: $%.2f" % (mins_extra, charge))
    total += charge

if texts_used > texts_incl:
    texts_extra = texts_used - texts_incl
    charge = texts_extra * add_text
    print("%.0f extra texts: $%.2f" % (texts_extra, charge))
    total += charge

# Applying tax multiliplier to total and printing output of total.
print("Sales tax at 5%")
total = total * tax_multi
print("Total: $%.2f" % total)
