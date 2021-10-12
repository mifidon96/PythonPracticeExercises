## A function that will capitalise letters, like in a predictive text app.
# The letters to be caapitalised: "i" with a space either side, the first
# character in the string and the first non-space character after ".", "!", or
# "?". The function returns the corrected string. Main() program reads the
# string, capitalises it using the function and displays the result. ##

def CapIt(string):
    test_str = string
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Capitalising a letter after ".", "!", or "?".
    for i in range(0,len(test_str)):
        if test_str[i] in ".!?":
            # Looking for first letter after punctuation, and only capitalising
            # if it is lowercase
            for j in range(i,len(test_str)):
                if test_str[j] in uppercase:
                    break
                if test_str[j] in lowercase:
                    test_str = test_str[0:j] + test_str[j].upper() + test_str[j+1:]
                    break

    # Capitalising first letter of string, same method as above
    for i in range(0,len(test_str)):
        if test_str[i] in uppercase:
            break
        if test_str[i] in lowercase:
            test_str = test_str[0:i] + test_str[i].upper() + test_str[i+1:]
            break

    # Capitalising " i "
    test_str = test_str.replace(" i ", " I ")
    test_str = test_str.replace(" i.", " I.")
    test_str = test_str.replace(" i?", " I?")
    test_str = test_str.replace(" i!", " I!")
    test_str = test_str.replace(" i,", " I,")

    return test_str


def main():
    string = input("Please enter a string: ")
    print(CapIt(string))


main()
