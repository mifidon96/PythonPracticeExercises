## A funtion that calculates the hypotenuse of a triangle, taking the lengths of
# the shorter sides as parameters (read from user in the main program), uses the
# pythagoras theorem and returns the hypotenuse length ##

# defining function, returning hypotenuse
def hyp(s_1,s_2):
    from math import sqrt
    s_3 = sqrt((s_1**2) + (s_2**2))
    return s_3


# Prompting user input
a = float(input("Input the length of side one: "))
b = float(input("Input the length of side two: "))

# Running function and displaying returned value.
print(hyp(a,b))
