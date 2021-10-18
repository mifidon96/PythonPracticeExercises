## 80 characters is usually the common width for a computer terminal but some
# screens can be wider or narrower, and as a result some text can be too long
# and wrap, making them difficult to read or too short and not make use of the
# available space. This is a program that opens a file and displays it so each
# line is used properly with no wrapping and using available space. Program must
# work correctly for files containing multiple paragraphs of text. Can detect
# paragraphs by looking for empty lines (once "\n" charcter removed) ##

# import modules
import sys

# Defining constants
TERM_CHAR_W = 50

with open(sys.argv[1]) as file:
    text_list = []
    char_count = 0

    for line in file:
        if line == "\n":
            if char_count > TERM_CHAR_W: # putting last word in paragraph that runs over
            # the threshold into a new display line
                insert = (text_list[-1].pop())
                text_list.append([insert])
                char_count = 0
            text_list.append([line])

        else:
            line_list = line.split() # Split the line into a list of words
            print("read line =", line_list)
            for word in line_list:
                if char_count == 0: # At start create new list containg first word
                    text_list.append([word])
                    char_count += len(word) + 1
                elif 0 < char_count <= TERM_CHAR_W: # if char_count is below or
                # == threshold then append this word to the display line list
                    text_list[-1].append(word)
                    char_count += len(word) + 1
                else: # If the char count is over threshold, start a new display
                # line containing the previous word that went over and the
                # current word
                    insert = (text_list[-1].pop())
                    text_list.append([insert])
                    text_list[-1].append(word)
                    char_count = 0 + len(insert) + len(word) +1

    if char_count > TERM_CHAR_W: # putting last word in paragraph that runs over
    # the threshold into a new display line
        insert = (text_list[-1].pop())
        text_list.append([insert])

    s = " "
    for item in text_list:
        print(s.join(item))
    print("\n", end="")
