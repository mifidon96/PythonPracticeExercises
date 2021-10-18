## Program that detects repeated words, displaying the line number and repeated
# word. Program should correctly handle when the repeated word is at the
# beginning of the new line. The file to be examined will be the only command
# line parameter. Display an appropriate error message if the user does not
# supply a command line parameter or if an error occurs when processing the file.
##

# importing modules and the onlyWords() function which splits lines into words
# only
import string
import sys
sys.path.append(r"C:\Users\ijmes_000\Desktop\Compsci\Python practice\BS Workbook\5 List exercises")
from Ex_111 import onlyWords

# Error message for no command line input.
if len(sys.argv) == 1:
    print("No input file detected.")
    quit()

try:
    with open(sys.argv[1]) as file:
        # Inititalising line number and the last word and empty lists to hold
        # the repeated word and it's line number at the same index
        rep_word_list = []
        rep_word_line_list = []
        line_num = 1
        last_word = ""
        # Reading each line, splitting into unpunctuated list of words, changing
        # word to ALL CAPS to match lettering only, checking current word
        # against last word, appending line number and word to lists then
        # updating last word. Updates the line number after each line processed.
        for line in file:
            line_list = onlyWords(line)
            for word in line_list:
                word = word.upper()
                if word == last_word:
                    rep_word_list.append(word)
                    rep_word_line_list.append(line_num)
                last_word = word
            line_num += 1

        # Displaying the repeated words and its corresponding line.
        if len(rep_word_list) == 0:
            print("No repeat words detected.")
        else:
            print("- Repeated words and line -")
            for i in range(len(rep_word_list)):
                print(f"{rep_word_list[i]}: line {rep_word_line_list[i]}")

except FileNotFoundError:
    print("file name invalid.")
    quit()
