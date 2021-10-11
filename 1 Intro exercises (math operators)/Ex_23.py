# Area of a regular polygon

from math import *

s = float(input("Please enter length of regular polygon side: "))
n = float(input("Please enter the number of sides: "))

a  = (n*(s**2))/(4*(tan(pi/n)))

print("The area of the regular polygon: %.2f" % a)
