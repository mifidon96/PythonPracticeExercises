## A program that determinnes if a string is a palindrome ##

# Prompting input from the user, converting string to lowercase characters, and
# determining the word length
entry = input("Enter a word: ")
word = entry.lower()
word_length = len(word)
# Checking if a word has an even or odd number of letters and determining half
# the number of letters in half of the word (either side of middle letter for
# on odd number word)

if word_length % 2 == 0: # Even
    half_word = int(word_length / 2)
else: # odd
    half_word = int((word_length - 1) / 2)

# Initializing palindrome to True
palindrome = True

# Comparing each letter working from the outside in. If the conditions for a
# palindrome are met, a holder variable (x) is set to 1. Else, var palindrome
# is set to False.
for i in range(0, half_word):
    if word[i] == word[len(word)-(i+1)]:
        x = 1
    else:
        palindrome = False

# Displaying output
if palindrome:
    print("\"%s\" is a palindrome" % entry)
else:
    print("\"%s\" is not a palindrome" % entry)
© 2021 GitHub, Inc.
Terms
Privacy
Security
