## Program that displays the key presses in order to type out a text on an old
# mobile phone. must handle upper and lowercase letters and ignoring any
# unspecified characters in brief e.g. ";" and "()" ##


num_pad = {1:".,?!:", 2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL", 6:"MNO", 7:"PQRS",
8:"TUV", 9:"WXYZ", 0:" "}

message = input("Please input a message: ") # Message input, converting to caps
message_cap = message.upper()
keys = ""

for c in message_cap: # reverse lookup method using dict.items() iterable
    for key, char in num_pad.items():
        if c in char:
            multi = char.index(c)+1
            keys += str(key)*multi

print(keys)
