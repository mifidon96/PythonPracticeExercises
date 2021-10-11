## A prgram that reads a letter grade from the computer then compute and display
# the equivalent grade points. An appropriate error message will appear if the
# user inputs an invalid letter grade ##

letter = input("Please input a capialised letter grade (e.g. A-): ")

if letter == "A+":
    score = 4.0
elif letter == "A":
    score = 4.0
elif letter == "A-":
    score = 3.7
elif letter == "B+":
    score = 3.3
elif letter == "B":
    score = 3.0
elif letter == "B-":
    score = 2.7
elif letter == "C+":
    score = 2.3
elif letter == "C":
    score = 2.0
elif letter == "C-":
    score = 1.7
elif letter == "D+":
    score = 1.3
elif letter == "D":
    score = 1.0
elif letter == "F":
    score = 0

print("%s is equivalent to %.1f grade points." % (letter, score))
