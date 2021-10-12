# Program that will dimulate 1,000 rolls of two dice. A function will simulate
# the rolling of a pair of six sided dice. Parameters: None. Returns: total score
#  main program will roll the dice 1,000 times, recording the number of times
# each score occurs. Then displays a table summarising the data, express
# frequency of each total as a percentage of the number of rolls, should also
# display the percentage expected by probability theory.

def dicePairRoll(): # Simulating rolling two dice
    from random import randint
    d1 = randint(1,6)
    d2 = randint(1,6)
    return d1 + d2

def main():
    rolls = int(input("How many times do you want to roll the dice: "))
    scores = {}

    for i in range(rolls): # Rolling dice and recording requency of score in a dictionary
        roll = dicePairRoll()
        if roll not in scores:
            scores[roll] = 1
        else:
            scores[roll] += 1

    scores_percent = {}  # Generating a dictionary of percentage frequencies
    for score, freq in scores.items():
        scores_percent[score] = [(freq/rolls) * 100]

    comb = 1 # Prdicting probability of getting each score
    for score in range(2,8):
        pred = (comb/36) * 100
        scores_percent[score].append(pred)
        comb += 1
    comb = 5
    for score in range(8,13):
        pred = (comb/36) * 100
        scores_percent[score].append(pred)
        comb -= 1

    # Displayiing table
    print("\nTotal    Simulated   Expected")
    print("           Percent    Percent")
    for i in range(2,13):
        # print("%d           %.2f       %.2f" % (i, scores_percent[i][0], scores_percent[i][1]))
        print("%5d %12.2f% 11.2f" % (i, scores_percent[i][0], scores_percent[i][1]))


if __name__ == "__main__":
    main()
