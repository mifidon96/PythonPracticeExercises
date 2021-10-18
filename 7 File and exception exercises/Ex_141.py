## Program that displays the first 10 lines of a file whend the filename is
# provided. Display an appropriate error message if the requested file does not
# exist or no command line entered ##

filename = input("Please enter a filename: ")

try:
    with open(filename) as f:
        for i in range(10):
            print(f.readline())

except FileNotFoundError:
    if filename == "":
        print("No filename entered.")
    else:
        print("This file does not exist.")
