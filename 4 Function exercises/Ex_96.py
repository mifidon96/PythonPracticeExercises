## A function that determines if a password is strong. Criteria are: at least 8
# characters, contains a least one upper and lower case letter, and at least one
# number. Parameter is password as a string, returns 'True' or 'False'. ##



def passIsStrong(s):
    import string
    # Innocent (True) until proven guilty (False) approach. Initializing
    # criteria check counters to 0.
    result = True
    lowerCheck = 0
    upperCheck = 0
    digitCheck = 0
    # Defining criteria
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    reqLength = 8
    # Checking length, and then checking character criteria, adding 1 to init 0
    # for each instance of a desired character
    if len(s) >= reqLength:
        for c in s:
            if c in lowercase: lowerCheck += 1
            elif c in uppercase: upperCheck += 1
            elif c in digits: digitCheck += 1
        # Any 0 value for criteria check means a weak password.
        if lowerCheck * upperCheck * digitCheck == 0:
            result = False
    else:
        result = False
    return result


def main():
    s = input("Enter a password: ")
    if passIsStrong(s):
        print("Password is strong")
    else:
        print("Password is weak")

if __name__ == "__main__":
    main()
