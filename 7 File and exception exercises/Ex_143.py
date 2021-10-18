## A program that concatenates and displays lines from different files, in the
# same order as the filenames are specified in the command line. Should generate
# an error message for any file that cannot be displayed then proceed to the
# next file. Also an error message for no file specified. ##

import sys

if len(sys.argv) == 1: # Error message for no file names passed
    print("No file names were specified in command line.")
    quit()

for file in sys.argv[1:]:
    try:
        with open(file) as f:
            #print("\n")
            for line in f:
                print(line)

    except FileNotFoundError:
        line = f"The file name entry at position {sys.argv.index(file)} \
        is invalid."
        print(line)
