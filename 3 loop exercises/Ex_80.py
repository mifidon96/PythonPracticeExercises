## A program that simulates a coin flip. It will also display the number of
# flips needed until tree consectutive results are reached. This will be done
# 10 times and then an average number will be reported. ##

from random import randint

av_total = 0
rounds = 300000


# running 10 rounds of flipping
for i in range(0,rounds):
    # First flip #########################################################
    flip = randint(1,2)
    if flip == 1:
        result = "H"
    else:
        result = "T"
    print("%s " % result, end="")

    # Setting last result (to be compared to) to result of the first flip. Initialising
    # consecutive counter and flip counter to 1
    last_result = result
    cons_count = 1
    flip_count = 1
    ######################################################################
    # Setting escape to three consecutive results
    while cons_count != 3:
        # flipping coin
        flip = randint(1,2)
        if flip == 1:
            result = "H"
        else:
            result = "T"
        print("%s " % result, end="")
        # Adding to consecutive counter or resetting to 1
        if result == last_result:
            cons_count += 1
        else:
            cons_count = 1
        # Setting the last result and adding one to flip counter
        last_result = result
        flip_count += 1

    # Displaying the number of flips for that round and adding that number to
    # total used to calculate average
    print("(%d flips)" % flip_count)
    av_total += flip_count
# Calculating and displaying average
av = av_total / rounds
print("On average,", av, "flips were needed.")
