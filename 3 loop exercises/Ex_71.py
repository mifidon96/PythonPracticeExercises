## A program that uses Newton's method to approximate the square root of a
# number. ##

# Prompting user for input
x = float(input("Enter a number: ")) #

#initializing first guess and calculating the limit
guess = x/2 #
print("Guess:", guess)
limit = abs((guess**2)-x)
print("Limit:", limit)

# loop with escape condition that absolute value of guess**2 and x is <= 10E-12
while limit > 10E-12:
    guess = (guess + (x/guess))/2
    print("Guess:", guess)
    limit = abs((guess**2)-x)
    print("Limit:", limit)
# Displaying output.
print("The square root of %f is %f (accurate to withing 10E-12)" % (x,guess))
