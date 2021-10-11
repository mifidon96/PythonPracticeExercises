# A program that determines if a liscence plate is old or new, or invalid.
# old plates are in the form XXXnnn, newer ones in the form nnnnXXX #

# prompt for user input
plate = input("Please enter a liscence plate registration number: ")

# Check to see plate rego is the right nuber of characters long.
# Running check for "old style" liscence plates

if len(plate) == 6:
    # Checking first three characters to enure they are capital letters
    invalid = False
    for i in range(0,3):
        if "Z" >= plate[i] >= "A":
            valid = True
        else:
            invalid = True
    # Checking last three characters to enure they are numbers
    for i in range(3,6):
        if "9" >= plate[i] >= "0":
            valid = True
        else:
            invalid = True
    # Displaying output message
    if invalid:
        print("This registration is not valid")
    else:
        print("This liscence plate is old.")

# Running identicL check for "new style" liscence plates
elif len(plate) == 7:
    invalid = False
    for i in range(0,4):
        if "9" >= plate[i] >= "0":
            valid = True
        else:
            invalid = True
    for i in range(4,7):
        if "Z" >= plate[i] >= "A":
            valid = True
        else:
            invalid = True
    if invalid:
        print("This registration is not valid")
    else:
        print("This liscence plate is new.")
# Output statement if registration does not comprise of 6 or 7 characters.
else:
    print("This registration is not valid")
