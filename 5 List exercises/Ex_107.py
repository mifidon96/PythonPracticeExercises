## A program that reads words from the user, and then displays them in order
# they were entered with repeats omitted. ##

list = []
entry = input("please enter a word: ")

while entry != "":
    if entry not in list:
        list.append(entry)
    entry = input("please enter a word: ")

print(list)
