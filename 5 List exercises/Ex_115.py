## A program that translates english into pig latin. 2 Rules of pig Latin:
#
# 1. If the word begins with a consonant (including y), then all letters at the
# beginning of the word, up to the first vowel (excluding y), are removed and
# then added to the end of the word, followed by ay. For example, computer
# becomes omputercay and think becomes inkthay.
#
# 2. If the word begins with a vowel (not including y), then way is added to the
# end of the word. For example, algorithm becomes algorithmway and office
# becomes officeway.
#
# Can assume string entered by user only contains lowercase letters and spaces.

# Defining vowels (not including y)
vowels = "aeiou"

# splitting up line in english into list of words and initializing empty pl list
e_line = input("Please enter a sentence (no Caps or punctuation): ")
e_line_list = e_line.split()
pl_line_list = []

# Checking each word and each letter in that world, then applying either rule 1.
# or 2. or no rules if not applicable to a word (e.g. the word "my") then adding
# the word to pl list.
for w in e_line_list:
    done = False
    for l in w:
        if l in vowels and not done:
            v_i = w.index(l)
            if v_i == 0: # Rule 2.
                w += "way"
                done = True
            else: # Rule 1.
                w = w[v_i:len(w)] + w[:v_i] + "ay"
                done = True
    pl_line_list.append(w)

# Joining up list using whitespace as dividor and displaying resultant string
pl_line = " ".join(pl_line_list)
print(pl_line)
