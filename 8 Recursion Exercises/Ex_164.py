## A program thta reads values from the user until a blank line is entered, and
# displays the total of all the values entered by the user (0.0 if first value
# is a blank line). USE RECURSION and no loops. ##

def adder():
    # Taking input as a string
    n = input("Please enter a number (blank to sum): ")

    # When a number is entered as a string it will be interpreted as a float and
    # the function will be called again to add another number to this value
    # This is the RECURSION CALL
    if n != "":
        n = float(n)
        return n + adder()
    # When a blank line is enterd then the function will return a zero and not
    # call the function again, effectively adding 0 to our current run of
    # additions and not call for the function to add anythin else. This is our
    # escape statement.
    else:
        return 0.0

print(adder())
Does not affect non-letters and can program can also be used to decode
