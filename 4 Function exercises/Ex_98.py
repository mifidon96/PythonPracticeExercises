## A function, hex2int, converts a string containing one single hexadecimal
# digit (upper and lowercase) to a base 10 integer . int2hex converts an integer
# between 0 and 15 into a string containing a single base 16 digit. Functions
# contain an error message for an invalid input and end the program.

def hex2int():
    # Defining criteria
    import string
    hex_uppercase = string.ascii_uppercase[0:6] # "ABCDEF"
    hex_lowercase = string.ascii_lowercase[0:6] # "abcdef"
    digits = string.digits
    length = 1
    # Prompting user input
    s = input("Please enter a single hexadecimal digit to convert to base 10: ")
    # Checking criteria
    if len(s) == length:
        if s in digits:
            result = int(s)
        elif s in hex_uppercase:
            result = hex_uppercase.index(s) + 10
        elif s in hex_lowercase:
            result = hex_lowercase.index(s) + 10
        else:
            print("This not a valid notation for a hexadecimal digit.")
            exit()
        print(s, "in base 10 is", result)
    elif len(s) == 0:
        print("No input detected.")
        exit()
    else:
        print("This program can only convert one digit at a time.")
        exit()

def int2hex():
    # Defining criteria
    import string
    hex_uppercase = string.ascii_uppercase[0:6] # "ABCDEF"
    max = 15
    # Prompting user input, checking for empty string
    s = input("Please enter a number between 0 and 15 to convert to hexadecimal: ")
    if s == "":
        print("No input detected.")
        exit()
    else:
        s = int(s)
    # Checking criteria
    if s <= max:
        if s <= 9:
            result = str(s)
        else:
            result = hex_uppercase[s-10]
        print(s, "in hexadecimal is", result)

    else:
        print("This number is outside of the specified range.")
        exit()

def main():
    hex2int()
    int2hex()

if __name__ == "__main__":
    main()
