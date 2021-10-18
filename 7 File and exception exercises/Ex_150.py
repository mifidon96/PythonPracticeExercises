## Program that removes the all of the comments from a python source file.
# Check each line to determine if there is a # in the line then remove the
# entire line. The modified file will be save using a name provided by the user.
# Ensure an appropriate error message is displayed if the file cannot be
# accessed. ##

filename_1 = input("Enter file to have comments removed: ")
filename_2 = input("Enter Save As filename: ")

try:
    with open(filename_1) as f:
        with open(filename_2, "a") as sf:

            for line in f:
                string = -1 # marker to detect "\""
                for c in line:
                    if c == "\"":
                        string *= -1
                    elif c == "#" and string == -1: # reading line up until #
                        hashtag_i = line.index("#")
                        line = line[:hashtag_i] + "\n"

                sf.write(line)

except FileNotFoundError:
    print("The file could not be found.")
    quit()
