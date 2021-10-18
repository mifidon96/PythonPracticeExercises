## A Spell checker that will check and display all misspelled words, comparing
# to the file, "words.txt". User will provide the name of the file in the
# command line, with an appropriate error message if the parameter is missing.
# Also an error message for if file could not be opened. Use solution to Ex_111
# so that words containg punctuation are not highlighted as spelling mistakes.
# Challenge says to ignore capitalization but I think I can handle it. ###

# Importing modules and importing onlyWords() function from Ex_111
import string
import sys
sys.path.append(r"C:\Users\ijmes_000\Desktop\Compsci\Python practice\BS Workbook\5 List exercises")
from Ex_111 import onlyWords

# Error message for no command line input.
if len(sys.argv) == 1:
    print("No input file detected.")
    quit()

typos = []

# Read line in file, apply onlyWords() to remove punctuation and split in to a
# list of words. Then check the word (its capitalized version and its
# lowercase form) to see if it exists in 'words.txt'. If not then add it to typos
# list and print it out.
with open("words.txt") as correct_words:
    try:
        with open(sys.argv[1]) as file:
            ########## putting words.txt into a list #########
            list_of_words = []
            for word in correct_words:
                word = word.rstrip("\n")
                list_of_words.append(word)
            #############################################################
            for line in file:
                line_list = onlyWords(line)
                for word in line_list:
                    word_forms = [word, word.capitalize(), word.lower(), word.upper()]
                    typo = True
                    for word_form in word_forms:
                        if word_form in list_of_words:
                            typo = False
                    if typo:
                        typos.append(word)

            if len(typos) > 0:
                print(f"List of typos:\n{typos}")
            else:
                print("No spelling errors detected.")

    except FileNotFoundError: # Detecting invalid filename
        print("File name is invalid.")
        quit()
