## A program that identifies the longest word(s) in a file. Output should
# display the length of the word(s) along with the word(s) with that length
# that appear in the file ##

import sys
import string

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("Invaid command")
    quit()

with open(filename) as f:
    long_words = []
    top_length = 0
    for line in f:

        for c in line: # Removing non letters from words
            if c not in string.ascii_letters or c != " ":
                line.replace(c, "")

        word_list = line.split() # Splitting line into list of words
        for word in word_list: # checking and updating longest word length and words
            if len(word) >= top_length:
                top_length = len(word)
                long_words.append(word)

    # longest_words = []
    # for word in long_words:
    #     if len(word) == top_length:
    #         longest_words.append(word)

    for i in range(len(long_words)):
        if len(long_words[i]) != top_length:
            long_words[i] = 0
    zeros = True
    while zeros:
        if 0 in long_words:
            long_words.remove(0)
        else:
            zeros = False


    print("Longest word(s) length:", top_length)
    # print("Longest word(s):", longest_words)
    print("Longest word(s):", long_words)
