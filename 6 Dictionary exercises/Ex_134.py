## Program that determines the number of unique characters in a string. e.g.
# "Hello, world!" has 10 unnique characters while "zzz" has one. ##

message = input("Enter a message: ")

chars = {}
chars = set()

for c in message:
    if c not in chars:
        chars.add(c)

print("Number of unique characters:", len(chars))
