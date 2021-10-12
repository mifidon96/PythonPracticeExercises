## Program that computes and displays the Scrabble score for a word (ignoring
# tile bonus.) ##

scrabble = {
1:["A", "E", "I", "L", "N", "O", "R", "S", "T", "U"],
2:["D", "G"],
3:["B", "C", "M", "P"],
4:["F", "H", "V", "W", "Y"],
5:["K"],
8:["J", "X"],
10:["Q", "Z"]
}

total = 0
word = input("Enter a word: ").upper()

for c in word:
    for num, letters in scrabble.items():
        if c in letters:
            total += num

print("The scrabble score for this word is:", total)
