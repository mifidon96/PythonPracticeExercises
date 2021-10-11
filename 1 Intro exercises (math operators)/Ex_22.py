## Program that determines the area of a triangle using lengths of all three
## sides as inputs

from math import *
# Taking user inputs
s1 = float(input("Please enter the length of the first side: "))
s2 = float(input("Please enter the length of the second side: "))
s3 = float(input("Please enter the length of the third side: "))

# Calculating using formula
s = (s1 + s2 + s3)/2
a = sqrt(s*(s-s1)*(s-s2)*(s-s3))

# Displaying output of equation
print("The area of the triangle is %.2f" % a)
