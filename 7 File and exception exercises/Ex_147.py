## A program that displays the word(s) that appear most in a file. Reading file
# from user. Not case sensitive, not including punctuation ##

import string

try:
    filename = input("Enter a file name: ")
    with open(filename) as f:

        word_freq = {} # Initializing word frequency dictionary
        for line in f: # formatting line to all lowercase and remving punct
            line = line.lower()
            for c in line:
                if c not in string.ascii_lowercase or c != " ":
                    line.replace(c,"")

            words = line.split() # Splitting line, looping and updating dict
            for word in words:
                if word not in word_freq:
                    word_freq.update({word:1})
                else:
                    word_freq[word] += 1

        top_freq = 0
        top_words = []
        for word in word_freq:
            if word_freq[word] > top_freq:
                top_freq = word_freq[word]
                top_words = [word]
            elif word_freq[word] == top_freq:
                top_words.append(word)

        if top_freq == 1:
            print("There is one of each word!")
        else:
            print("Most frequent word(s):", top_words)

except FileNotFoundError:
    print("File entry invalid.")
