## Program that determines the volume of a cylinder from a radius and height
# value input. Returns value to one decimal place.
from math import pi

# inputs
r = float(input("Please input radius value: "))
h = float(input("Please input a height value: "))

# formula
area = pi*r**2
vol = area*h

# Print output
print("Volume of cylinder: %.1f" % vol)
