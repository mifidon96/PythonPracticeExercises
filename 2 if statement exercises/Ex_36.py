# Program thay determinese whether a letter input by the user is a vowel or a
# consonant, with "y" as a special case

letter = input("Please enter a letter: ")

if letter in ["a", "e", "i", "o", "u"]:
    case = "a vowel"
elif letter == "y":
    case = "sometimes a vowel, sometimes a consonant."
else:
    case = "a consonant"

print("This letter is", case)
