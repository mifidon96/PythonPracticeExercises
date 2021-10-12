## A function that formats a ste of strings into a comma separated sentence with
# an "and" before the final word e.g. "apples, oranges, pears and bananas"
# Parameter: a list of strings. Returns: a string of the formatted sentence.
# main() program will read several items form the user, uses funciton to format
# the list then displays the returned string. ##


def formatList(l):
    string = ""
    for w in l:
        string += w
        if l.index(w) == len(l) - 2:
            string += " and "
        elif l.index(w) == len(l) - 1:
            string += ""
        else:
            string += ", "

    return string

def main(): # Reads words from user, puts them in a list, applies format function
     l = []

     entry = input("Please enter a word (blank to quit): ")
     while entry != "":
         l.append(entry)
         entry = input("Please enter a word (blank to quit): ")
     print(formatList(l))

if __name__ == "__main__":
    main()
