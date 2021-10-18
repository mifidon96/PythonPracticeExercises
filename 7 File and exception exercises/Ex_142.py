## This program will return the last 10 ines of a file. With error messages
# for an invalid file name or a blank input. Ben has said that there are two
# not so good ways to tackle this...
# 1: load the entire contents of the file into a list and then display the
# last ten elements.
# 2: Read the contents of the file twice, once to determine the number of lines
# and then again to just read the last 10.
# These methods are not desirable when reading large files. Apparently there
# is a way to do it by reading the file only once and only requires you to store
# 10 lines from the file at one time. "For an added challenge, develop such a
# solution." I will have a go!

# Thinking of going down from beginning, storing the first ten and then
# continuing down the file, deleting the first line and adding the next. Once
# all the lines are read the var will hold the last ten lines.

filename = input("Please enter a filename: ")

try:
    with open(filename) as f:
        lines = []
        while len(lines) <= 10:
            entry = f.readline()
            lines.append(entry)
            if entry == "":
                break
            elif len(lines) > 10:
                del lines[0]

        for line in lines:
            print(line)

except FileNotFoundError:
    if filename == "":
        print("No file name given.")
        quit()
    else:
        print("Invalid file name.")
        quit()
