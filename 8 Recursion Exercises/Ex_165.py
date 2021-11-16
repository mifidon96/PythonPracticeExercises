## A program that uses Euclid's algorithm to compute th greatest common divisor
# of two positive integers entered by the user ##

def euclid(a,b):
    if b == 0:
        return a
    else:
        c = a % b
        return euclid(b,c)

a = float(input("Please enter the first integer: "))
b = float(input("Please enter the second integer: "))

print(euclid(a,b))

### In this exercise euclid's algorithm was provided but you had to write it
# with a recursive call ###
