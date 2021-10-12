## A program that displays the average of a set of values, then all of the below
# average values, then the average values (either the exact value or two values
# either side of the average), then all the above average values, all with
# apropriate labels. ##

# Set up list of sample data and fill list with user inputs
sample = []

entry = input("Please enter a number (blank line to quit): ")
while entry != "":
    entry = float(entry)
    sample.append(entry)
    entry = input("Please enter a number (blank line to quit): ")

# Sorting sample data into ascending order and calculating mean average
sample.sort()
av = sum(sample)/len(sample)

# Initialising below and above averege value lists
b_av = []
a_av = []

# Appending values to b/a average value lists. If average exists in sample data
# then avs list is simply that value, if not then using pop of last/first
# element of below/above average values resp. to get the two average values.
for e in sample:
    if e < av:
        b_av.append(e)
    elif e > av:
        a_av.append(e)
if av in sample:
    avs = [av]
else:
    avs = [b_av.pop(), a_av.pop(0)]

# Displaying output
print("Mean average: %.2f" % av)
print("Below average values: \n", b_av)
print("Average values: \n", avs)
print("Above average values: \n", a_av)
