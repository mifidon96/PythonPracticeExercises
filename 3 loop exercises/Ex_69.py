# A program that computes 15 approximations of pi, with increasing accuracy #

# Initialize pi approximation to 3, and term positive term sign to 'True'
pi = 3
positive = True

# start to add the terms, starting with n == 2 up to 30 in steps of 2 (15
# iterations)
for n in range(2,31,2):
    term = 4/(n*(n+1)*(n+2))
    # Conditions for adding or subtracting term
    if positive:
        pi += term
    else:
        pi -= term
    # Flipping sign of term on each pass of loop and displaying approximation
    # of pi
    positive = not positive
    print(pi)
