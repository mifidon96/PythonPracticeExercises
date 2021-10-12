## Program that simulates a game of bingo, using a shuffled list of all valid
# bingo calls (B1 through O75) per game and 'crossing out' numbers. The Program
# will simulate 1000 games and report the minimum, maximum and average number of
# calls until a game is won. ##

# imports
import random
from Ex_138 import genBingoCard
from Ex_138 import displayBingoCard
from Ex_139 import bingoCheck

# Stats initalisation
call_count_list = []

# Generating a list of all possible calls
calls = []
num = 1
for letter in "BINGO":
    for i in range(15):
        num_entry = str(num)
        calls.append(letter+num_entry)
        num += 1


# Simulating 100 games
for i in range(1000):
    random.shuffle(calls) # Shuffling our call list
    shuffled_calls = list(calls) # NEED TO DO THIS TO MAKE A COPY OF THE LIST
    card = genBingoCard() # generating our card
    win = bingoCheck(card) # checking if it is a win (won't be at this point)
    call_count = 0 # Initializing the count for the number of calls

    while not win:
        call = shuffled_calls.pop(0) # making a call
        letter = call[0] # Separating letter (str) from number (int)
        num = int(call[1:])

        if num in card[letter]: # Checking if we have a match
            index = card[letter].index(num)
            card[letter][index] = 0
        call_count += 1
        win = bingoCheck(card)

    call_count_list.append(call_count)

# Finding the minimum, maximum and average number of calls to win a game of bingo.
max_calls = max(call_count_list)
min_calls = min(call_count_list)
av = sum(call_count_list)/len(call_count_list)

# Displaying output
print("Average amount of calls needed to win a game: %.2f" % av)
print("Minimum amount of calls needed to win a game: %d" % min_calls)
print("Average amount of calls needed to win a game: %d" % max_calls)
