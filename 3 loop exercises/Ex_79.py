## A program that sorts 100 random integers between 1 and 100 in order. A specific
# algorithm is specified: whereby a random number genreator produced a random
# number, saves it as the largest number, and then generates 99 more, evaluating,
# whether it is the largest number each time. On each generation the number should
# be displayed, if the largest number value is updated then this should be
# displayed too. At the end of the loop the max value should be displayed and
# the number of updates made. ##

from random import randint

# generatingn first random number, setting to max and printing
n = randint(1,100)
max = n
print(n)
count = 0

# Looping through 99 more iterations, making checks for larger number and updating
# max. Also counting number of updates.
for i in range(1, 100):
    n = randint(1,100)
    if n > max:
        max = n
        print(n,"<= update")
        count += 1
    else:
        print(n)

# Output displayed
print("\nMaximum vale:", max)
print("Number of updates:", count)
