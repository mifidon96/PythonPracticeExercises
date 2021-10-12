# Program that computes the perimeter of a polygon from co-ordinates entered
# by the user #

from math import *

# Taking initial x and y values from the user and setting them to end point,
# and "prev co-ordinates" to be used in the calculation
x_0 = x_o = float(input("Enter the x part of the co-ordinate: "))
y_0 = y_o = float(input("Enter the y part of the co-ordinate: "))
# iinitializing the value of x and perimeter running total
x = 0
total_d = 0
# looping and taking x reading from user, while entry is not an empty string
while x != "":
    x = input("Enter the x part of the co-ordinate (blank to quit): ")
    if x!= "":
        # converting x and y inputs to floats
        x = float(x)
        y = float(input("Enter the y part of the co-ordinate: "))
        # plugging in new and previous x and y values into equation
        d = sqrt(((x-x_o)**2)+((y-y_o)**2))
        # adding to running total
        total_d += d
        # setting x and y inputs to "previous" values to be used in the next calc
        x_o = x
        y_o = y
# Once loop is broken, using the end point (and start) along with most recent
# co-ordinate set from loop to find the last distance and then adding it to total
final_d = sqrt(((x_0-x_o)**2)+((y_0-y_o)**2))
total_d += final_d
# Displaying output
print("Perimeter of polygon is: %f" % total_d)
