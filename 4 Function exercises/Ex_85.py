## Function that takes and integer as its onlyy parameter and reterns a string
# containing its ordinal number word (e.g "first", "second") for numbers 1 - 12.
# returns an empty string if parameter number ist outside this range.
# Main program displays each integer in range and its ordinal number. ##

def ord(x):
    if x == 1:
        return "First"
    elif x == 2:
        return "Second"
    elif x == 3:
        return "Third"
    elif x == 4:
        return "Fourth"
    elif x == 5:
        return "Fith"
    elif x == 6:
        return "Sixth"
    elif x == 7:
        return "Seventh"
    elif x == 8:
        return "Eighth"
    elif x == 9:
        return "Ninth"
    elif x == 10:
        return "Tenth"
    elif x == 11:
        return "Eleventh"
    elif x == 12:
        return "Twelfth"
    else:
        return ""

def main():
    for i in range(1,13):
        ordinal = ord(i)
        print(i, ordinal)
