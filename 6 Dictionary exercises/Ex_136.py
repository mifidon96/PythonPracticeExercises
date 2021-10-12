## A program that can check if two phrases are anagrams ##

message_1 = input("Enter a phrase: ") # Reading input from user
message_2 = input("Enter another phrase: ")

punct = ";:'.,!?" # Making all caps, removing punctuation and white space
message_1, message_2 = message_1.upper(), message_2.upper()
message_1 = message_1.replace(" ","")
message_2 = message_2.replace(" ","")

for p in message_1:
    if p in punct:
        message_1 = message_1.replace(p,"")
for p in message_2:
    if p in punct:
        message_2 = message_2.replace(p,"")

set_1, set_2 = {}, {} # Making dictionaries to record freq of unique characters
anogram = True # Initializing anogram state

if len(message_1) != len(message_2): # If phrases not of same length,
# cannot be anograms
    anogram = False

for c in message_1: # Entering unique characters for both phrases with frequency
    set_1.update({c:0})
for c in message_1:
    if c in set_1:
        set_1[c] += 1

for c in message_2:
    set_2.update({c:0})
for c in message_2:
    if c in set_2:
        set_2[c] += 1

for i in set_1.items(): # comparing the two ditionaries.items() against eachother
    if i not in set_2.items():
        anogram = False
for i in set_2.items():
    if i not in set_1.items():
        anogram = False

if anogram: # Display
    print("The phrases are anograms!")
else:
    print("The phrases are not anograms.")
