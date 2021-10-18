## A program that reads a file of chemical elements, each line consisting of:
# Atomic number, Chemical Symbol, Element name
# And store this in appropriate data structures. If the user types in a piece of
# data then the program should display the other two pieces, e.g. user types in
# an integer, then the program will display the symbol and name corresponding to
# this atomic number, etc etc. Appropriate error message for a bad input. Keep
# working until a blank line is entered. ##

import csv
# Initializing data lists, with paceholders for index 0, so Hydrogen can match
# index 1 (Atomic number 1)
Ans = [0]
syms = ["-"]
names = ["-"]

with open("elements.txt") as f: # Reading file and forming data lists
    csv_reader = csv.reader(f)
    for line in csv_reader:
        Ans.append(int(line[0]))
        syms.append(line[1])
        names.append(line[2])

lookup = "A"
while lookup != "":
    lookup = input("Enter Atomic number, Symbol or Name: ")
    try: # Attmpting to interpret input as an integer, if so looking for sym and name
        lookup = int(lookup)
        output = f"Element: {names[lookup]}, Symbol: {syms[lookup]}"

    except: # if not an integer, first trying to look up in syms
        lookup = str(lookup)
        lookup = lookup.capitalize()
        if lookup in syms:
            i = syms.index(lookup)
            output = f"Element: {names[i]}, A-n: {Ans[i]}"
        elif lookup in names: # if not in syms then attempting lookup in names
            i = names.index(lookup)
            output = f"Symbol: {syms[i]}, A-n: {Ans[i]}"
        else: # error message for no match in the three lists.
            print("Invalid input")
            quit()

    print(output)
