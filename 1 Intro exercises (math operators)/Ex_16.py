# program that calculates the area of a circle and the volume of a sphere from
# a radius provided by the user

from math import *
r = float(input("Please enter a radius r: "))

area = pi*r**2
vol = (4/3)*pi*r**3

print("Area of circle: %.2f" % area)
print("Volume of sphere: %2f" % vol)
