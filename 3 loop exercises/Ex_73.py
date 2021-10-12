## A program that also determines a palindrome (Just like in Ex_73) but now
# ignores spaces an punctuation in order to process whole phrases. This uses
# and extends the code from Ex_72. ###

# Defining all lowercase letters and initializing the checkable string to an
# empty string
lowercase = "abcdefghijklmnopqrstuvwxyz"
check_str = ""

# Prompting user input for the entry to be tested and converting all letters in
# the entry to lowercase (into var line)
entry = input("Enter a word or phrase: ")
line = entry.lower()

# From var line, exctracting lowercase letters only. Concatinating these letters
# into str check_str
for l in line:
    if l in lowercase:
        check_str += l

# Initializing palindrome to True
palindrome = True

# Looping through str check_str to identify if it is a palindrome.
for i in range(0, len(check_str) // 2):
    if check_str[i] != check_str[len(check_str) - i - 1]:
        palindrome = False

# Displaying output.
if palindrome:
    print("\"%s\" is a palindrome" % entry)
else:
    print("\"%s\" is not a palindrome" % entry)
