## Program which collects data points from the user (x and y co-ords) and
# calculates a line of best fit (ybar = m * xbar + c) where xbar and ybar are
# the average x and y co-ords, and using a provided formula provided to find the
# value for m and c. The program will read the x and y co-ords separately, one
# data point at a time, until a blank line is enterd. program wil display the
# formula for the line. ##

# Initializing data point count (n) and x and y lists
n = 1
x = []
y = []

x_entry = input("Please enter x co-ordinate for data point %d (blank to quit): " % n)
while x_entry != "":
    x_entry = float(x_entry)
    y_entry = float(input("Please enter y co-ordinate for data point %d (blank to quit): " % n))
    x.append(x_entry)
    y.append(y_entry)
    n += 1
    x_entry = input("Please enter x co-ordinate for data point %d (blank to quit): " % n)
n -= 1

if n < 2:
    print("Not enough data points.")
    quit()

# Calculating ybar = m * xbar + c.
ybar = sum(y)/n
xbar = sum(x)/n
# First calculating terms for m
SIG_xy = 0
xy_pairs = list(zip(x,y))
for pair in xy_pairs:
    SIG_xy += pair[0] * pair[1]
SIG_x_SIG_y_over_n = (sum(x) * sum(y))/n
SIG_xsquared = 0
for number in x:
    SIG_xsquared += number**2
SIGx_squared_over_n = (sum(x)**2)/n
# calculating m
m = (SIG_xy - SIG_x_SIG_y_over_n)/(SIG_xsquared - SIGx_squared_over_n)
# calculating c
c = ybar - m * xbar

# Displaying output
print("Equation for LOBF: y = %.2fx + %.2f" % (m , c))
