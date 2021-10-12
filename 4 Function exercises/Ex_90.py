## Function that determines wether or not a string represents a valid integer.
# Function ignores white space, string must be at ease one character long,
# contains only digits, or if first character is +/- followed by digits. ##

def isInteger(string):
    Integer = True
    # Removes leading and trailing white space
    string_test = string.strip()
    # Defining set of valid integer characters
    prefix = "+-"
    numbers = "0123456789"
    # Testing to see if there is a prefix, and if so, removing from test string
    if string_test[0] in prefix:
        string_test = string_test[1:]
    # Looping through and seeing if characters in test_string are numbers only
    for c in string_test:
        if c not in numbers:
            Integer = False
    return Integer

def main():
    string = input("Enter an integer: ")
    if isInteger(string):
        print("This is an integer")
    else:
        print("This is not an integer")

# This command stops the main() function being run automatically if this file is
# imported
if __name__ == "__main__":
    main()
