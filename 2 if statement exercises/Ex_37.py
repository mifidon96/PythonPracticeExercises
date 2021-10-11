# A program that determines the name of a shape based on the number of sides
# entered by the user

sides = int(input("Please enter the number of sides that your shape has: "))

if 11 > sides >= 3:
    if sides == 3:
        print("The shape is a triangle!")
    elif sides == 4:
        print("The shape is a quadrilateral!")
    elif sides == 5:
        print("The shape is a pentagon!")
    elif sides == 6:
        print("The shape is a hexagon!")
    elif sides == 7:
        print("The shape is a heptagon!")
    elif sides == 8:
        print("The shape is an octagon!")
    elif sides == 9:
        print("The shape is a nonagon!")
    else:
        print("The shape is a decagon!")
else:
    print("I do not know that shape.")
