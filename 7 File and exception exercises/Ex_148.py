## Program that sums all numbers entered by the user, ignoring any entries
# that are not not valid numbers and display an appropriate error message.
# Program should display running total after each entry and exit when blan line
# is entered. Program should work correctly for both integers and floating point
# numbers. ##

import string

total = 0
invalid_num = False
floating_point = False
valid_chars = string.digits + "."

num = input("Enter a number: ")
while num != "":
    for c in num:
        if c not in valid_chars and not invalid_num: # Checking for valid characters
            print("This is not a valid number.")
            invalid_num = True
    if not invalid_num:
        if "." in num or floating_point == True : # Checking for decimal point
        # or a float has already been entered. Changing total to a float.
            total = float(total) + float(num)
            floating_point = True
        if not floating_point:
            total += int(num)
        print("Running total:", total)

    invalid_num = False
    num = input("Enter a number: ")
print("Total:", total)
