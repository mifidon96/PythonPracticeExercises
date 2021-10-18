## Program that determines the frequency of all letters found in the file.
# Should not be case sensitive and exclude all characters that are not letters.
# The file name should be specified in the command line, with error messges. ##

import sys
import string

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("Please only enter one file in the command line.")
    quit()

try:
    filename = sys.argv[1]
    with open(filename) as f:

        letter_freq = {} # Initializing letter frequency dictionary
        for l in string.ascii_uppercase:
            letter_freq.update({l:0})

        text = f.read() # Reading all text, converting to CAPS recording freq
        text = text.upper()
        for c in text:
            if c in string.ascii_uppercase:
                letter_freq[c] += 1

    print(letter_freq)

except FileNotFoundError:
    print("File entry invalid.")
