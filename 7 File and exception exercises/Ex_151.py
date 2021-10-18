## A program that generates a password by randomly selecting two english words
# and concatinating them together. Ensuring that the entire length is between
# 8 to 10 characters long, and that each word is at least three letters long.
# Capitalising each word so the user can easily see each word and hence will be
# easier to memorise. Display password to user. Using the file "words.txt" in
# the program directory. ##

from random import randint

with open("words.txt") as f:
    # Constants
    UPPER_LEN = 10
    LOWER_LEN = 8
    MIN_WORD_LEN = 3
    MAX_WORD_LEN = 7
    LEN_FILE = 0
    for line in f:
        LEN_FILE += 1
    f.seek(0,0)
    PASS_LEN = randint(8,10)

    # Finding first word: Selecting a random start line number, reading lines
    # and setting first word to the first line read that is an appropriate
    # length and is either on or after the start line.
    start_i = randint(0,LEN_FILE-1)
    i = 0
    for line in f:
        i += 1
        line = line.rstrip() # REMOVING NEW LINE CHARACTER
        if i >= start_i and len(line) >= MIN_WORD_LEN and len(line) <= MAX_WORD_LEN:
            word_1 = line
            break

    f.seek(0,0) # Retettig read/write marker to beginning of file.
    # Same method for finding second letter but now ensuring sum of the two word
    # lengths is equal to the randomly sleceted password length (within range)
    start_i = randint(0,LEN_FILE-1)
    i = 0
    for line in f:
        i += 1
        line = line.rstrip() # REMOVING NEW LINE CHARACTER
        sum = len(word_1) + len(line)
        if i >= start_i and sum == PASS_LEN:
            word_2 = line
            break

word_1, word_2 = word_1.capitalize(), word_2.capitalize()
print(f"Password: {word_1 + word_2}")
