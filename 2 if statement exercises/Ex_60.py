# Program that simulates a spin of a roulette wheel

from random import *
# creating list of red and black numbers
red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
black = [2,4,5,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
# pseudo random number generator for simulated spin
spin = randint(0,37)

# 0 and 00 check
if spin == 0:
    print("The spin resulted in", spin)
    print("Pay 0")
elif spin == 37:
    print("The spin resulted in 00")
    print("Pay 00")
else:
    # Colour check
    if spin in red:
        colour = "Red"
    elif spin in black:
        colour = "Black"
    #  Odd/even check
    if spin % 2 == 0:
        num = "Even"
    else:
        num = "Odd"
    # Range check
    if 1 <= spin <= 18:
        range = "1 to 18"
    elif 19 <= spin <=36:
        range = "19 to 36"
    # Output display
    print("The spin resulted in", spin)
    print("Pay", spin)
    print("Pay", colour)
    print("Pay", num)
    print("Pay", range)
