## A program that reads python source files and determines if there are
# functions declared which are not immediately preceeded by a comment.
# The program will display the names of the functions that are missing comments
# and the file name and line number where the funciton is defined.
# Assuming any line that begins with "def ", including the space, is the beggining of
# a funciton definition. Assume that the comment character "#" will be the first
# character on the previous line. User will provide filenames as command line
# parameters. Display appropriate error messages for files that do not exist or
# cannot be opened before processing the rest of the files. ##

import sys

if len(sys.argv) == 1:
    print("No files specified.")
    quit()

for input_file in sys.argv[1:len(sys.argv)]:
    try:

        with open(input_file) as file: # opening file to be examined
            uncomm_funct_list = [] # List to store name of funct and line
            line_num = 1 # initialising line number
            prev_line_char = "" # initialising prev line first character

            for line in file:
                if line != "\n":
                    # Checking if "def " is the first thing on line, and prev line
                    # is not a comment. If so then add the name of the function and
                    # the line number it is found on to the list as a tuple
                    line_list = line.split()
                    if line_list[0] == "def" and prev_line_char != "#":
                        uncomm_funct_list.append((line_list[1],line_num))

                    # updating the line number and the first character of previous line
                    line_num += 1
                    prev_line_char = list(line_list[0])[0]
            if len(uncomm_funct_list) > 0:
                print(f"{input_file} has the following uncommented functions:")
                for entry in uncomm_funct_list:
                    print(f"{entry[0]} at line {entry[1]}")
                    print("\n")
            else:
                print(f"{input_file} has no uncommented functions.\n")

    except FileNotFoundError:
        print(f"{input_file} is invalid.\n")
