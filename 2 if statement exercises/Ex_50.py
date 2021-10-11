# A program that computes the real roots of a quadratic function using the
# discriminant(sqrt(b**2-4ac)) to evaluate the number of roots. -ve = no real
# roots, 0 = one real root and +ve = two real roots. #

from math import *
# prompting user input
a = float(input("Please enter an \"a\" value for ax**2 + bx + c: "))
b = float(input("Please enter an \"b\" value for ax**2 + bx + c: "))
c = float(input("Please enter an \"c\" value for ax**2 + bx + c: "))
# defining the descriminant
disc = (b**2)-4*a*c
# conditions for discriminant followed by applicable calculation and output
# display
if disc == 0:
    root = -b/2*a
    print("There is one real root for this equation and it is", root)
elif disc > 0:
    root1 = (-b+sqrt(disc))/2*a
    root2 = (-b-sqrt(disc))/2*a
    print("There are two real roots for this equation and they are", root1, "and", root2)
else:
    print("There are no real roots")
