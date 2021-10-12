## A program that determines if two words are anagrams ##

# Taking user input and initialising dictionaries
message_1 = input("Enter a word: ")
message_2 = input("Enter another word: ")
message_1, message_2 = message_1.upper(), message_2.upper()
set_1, set_2 = {}, {}

anogram = True # Initializing anogram state

if len(message_1) != len(message_2): # If words are not same length they can't
# be anograms
    anogram = False

for c in message_1: # Entering each unique letter
    set_1.update({c:0})
for c in message_1: # Adding frequency to each letter
    if c in set_1:
        set_1[c] += 1

for c in message_2:
    set_2.update({c:0})
for c in message_2:
    if c in set_2:
        set_2[c] += 1

for i in set_1.items(): # checking a dict.items() list against eachother.
    if i not in set_2.items():
        anogram = False
for i in set_2.items():
    if i not in set_1.items():
        anogram = False

if anogram: # Display output
    print("The words are anograms!")
else:
    print("The words are not anograms.")
