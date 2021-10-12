## Pig latin improved: The Program. extending solution to Ex_115 so it handles
# capital letters and punctuation ##

# Defining vowels (not including y), punct found after a word, and caps.
vowels = "aeiou"
punct_after = ",.?!:;"
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# splitting up line in english into list of words and initializing empty pl list
e_line = input("Please enter a sentence: ")
e_line_list = e_line.split()
pl_line_list = []

# Checking each word and each letter in that world, then applying either rule 1.
# or 2. or no rules if not applicable to a word (e.g. the word "my") then adding
# the word to pl list.
for w in e_line_list:
    capital = False
    done = False
    punct_hold = ""
    for c in w: # Checking if a letter is capitalised (assuming it is the
    # first letter) then converting all letters to lowercase in the word.
        if c in caps:
            capital = True
            w = w.lower()
        if c in punct_after: # Finding punctuation, assigning it to a var then
        # removing from word
            punct_i = w.index(c)
            punct_hold = w[punct_i]
            w = w.replace(c,"")
        if c in vowels and not done:
            v_i = w.index(c)
            if v_i == 0: # Rule 2.
                w += "way"
                done = True
            else: # Rule 1.
                w = w[v_i:len(w)] + w[:v_i] + "ay"
                done = True

    if capital: # If capital detected then first letter of pl word is capitalised
        w = w.capitalize()
    w += punct_hold # Adding on punctuation
    pl_line_list.append(w)

# Joining up list using whitespace as dividor and displaying resultant string
pl_line = " ".join(pl_line_list)
print("\n%s" % pl_line)
