# A program that takes in a denomination of money in $US and returns the name
# of the person displayed on the note.

# Creating the lists for people who appear on $US dollar bills and their
# corresponding monetary values.
people = ["George Washington.", "Thomas Jefferson.", "Abraham Lincoln.", \
"Alexander Hamilton.", "Andrew Jackson.", "Ulysses S. Grant.", "Benjamin Franklin."]
denom = [1, 2, 5, 10, 20, 50, 100]
# Prpmpting user input for an amount
note = int(input("Please input a paper denomination of $US: "))
# Checking to see if denomination entered is valid and if so then taking the
# corresponding person from people list using the same index. Also displaying
# error message if not.
if note in denom:
    person = people[denom.index(note)]
    print("The person on this note is", person)
else:
    print("I'm sorry but that dollar bill does not exist.")
