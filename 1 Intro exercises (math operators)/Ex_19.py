## Program that calculates the final velocity of an object accelerating under
## earth's gravity from rest

from math import *
#Initializing constants
a = 9.8
vi = 0
# User input for height
d = float(input("Please enter the hieght (in meters) from which the object is dropped: "))
# Calculation using formula
vf = sqrt(vi**2+2*a*d)
# Output
print("The final velocity is: %.2f m/s" % vf)
