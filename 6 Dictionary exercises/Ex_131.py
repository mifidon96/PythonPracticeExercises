## Program that translates a message into morse code, leaving a space between
# letters, should ignore any characters that are not letters or numbers. ##

morse_table = {"A":".-", "B":"-..", "C":"-.-.", "D":"-..", "E":".", "F":"..-.",
"G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--",
"N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-",
"U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..",
"0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....",
"6":"-....", "7":"--...", "8":"---..", "9":"----.", }

message = input("Enter a message: ")
message = message.upper()
morse = ""

for c in message:
    if c in morse_table:
        morse += morse_table[c] + " "

print(morse)
