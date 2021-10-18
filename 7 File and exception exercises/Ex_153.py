## A program that reads words from a text file and "determines how many words use
# each letter of the alphabet." I am assuming this means tallying the number of
# times a letter is used by a word, not counting repeated letters in each word.
# Include an additional message about the letter that is used the most and least.
# Ignore punctuation and upper/lowercase. ###

import string

letters = string.ascii_uppercase
record = {}
for l in letters:
    record.update({l:0})
pl_l, pl_t = "", ""

filename = input("Enter file name: ")

with open(filename) as f:
    for line in f:
        line = line.upper().rstrip() # removing"\N"
        line_list = line.split()
        for word in line_list:
            for l in letters:
                if l in word:
                    record[l] += 1

top_letter = max(record.keys(), key=(lambda k: record[k]))
least_letter = min(record.keys(), key=(lambda k: record[k]))

least_letters = []
top_letters = []
for i in record:
    if record[i] == record[least_letter]:
        least_letters.append(i)
    if record[i] == record[top_letter]:
        top_letters.append(i)

if len(least_letters) > 1:
    least_letter = least_letters
    pl_l = "s"
if len(top_letters) > 1:
    top_letter = top_letters
    pl_t = "s"

print(f"\nProportion of words that use letter:\n{record}\n \
\nMost used letter{pl_t}: {top_letter} \
\nLeast used letter{pl_l}: {least_letter}")
