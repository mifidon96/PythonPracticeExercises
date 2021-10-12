## Program that converts binary into decimal numbers ##

# prompt input from user for string
n_b = input("Please input a binary number: ")

# initilising total to 0 and place value to 1.
total = 0
p_v = 1

# looping through the inputted string: starting at the last character in the
# string (right-most character), proceeding in steps of -1 to the first
# character (left-most character); checking for "1" and adding p_v to total if
# true. p_v multiplied by 2 (because binary notation) on each pass of loop.
for i in range(len(n_b)-1,-1,-1):
    if n_b[i] == "1":
        total += p_v
    p_v *= 2

# Displaying output
print("The number in decimal is", total)
