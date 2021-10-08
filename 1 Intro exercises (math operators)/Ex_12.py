# program that finds the distance between two points on earth from an input
# of start and finish latitude and longitude values

#asking user for latitude and longitude values and converting degress into
# radians

from math import *

t1 = radians(float(input("please enter your start latitude:")))
g1 = radians(float(input("please enter your start longitude:")))
t2 = radians(float(input("please enter your finish latitude:")))
g2 = radians(float(input("please enter your finsih longitude:")))

# using formula to convert

distance = 6371 * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1-g2))
print("distance is %.2f km" % distance)
