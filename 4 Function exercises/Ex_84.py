# A function that takes three numbers as parameters and returns the median #

# Defining function, ataking three numbers as parameters.
def med(a,b,c):
    # Setting parameters to floats
    a, b, c = float(a), float(b), float(c)
    # Using xor operator on x > other two values (median in a set of three
    # numbers)
    if (a > b) ^ (a > c):
        return a
    elif (b > a) ^ (b > c):
        return b
    elif (c > a) ^ (c > b):
        return c

# Propmting user input
a = input("Please enter the first number: ")
b = input("Please enter the second number: ")
c = input("Please enter the third number: ")

# Running function and displaying output
median = med(a,b,c)
print("The median value is", median)
