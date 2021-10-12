## A function that identifies all of the words in a string entered by the user.
#  Parameter: a string. Returns: a list of words in the string with the
# punctuation marks at the edges of words removed including (,.?-'!:;) except
# for apostraphes in the middle of words e.g. don't, can't etc. main() program
# demonstrates the function, and only runs when not imported. ##

def onlyWords(s):
    # Defining puntuation to be removed including ' when not following a letter.
    punct = ["," , "." , "?" , " -" , "!" , ":" , ";" , " '"]
    # replacing all instances with an empty string
    for p in punct:
        s = s.replace(p,"")
    # Splittling string and returning list
    list = s.split()
    return list

def main():
    s = input("Please enter a sentence: ")
    print(onlyWords(s))

if __name__ == "__main__":
    main()
