## Program that redacts sensitive words from a text file by replacing each letter
# with an asteriks "*". Program should redact sensitive words hidden in other
# words and not be case sensitive. List of sensitive words will be provided in
# a separate text file (each line will be a word). redacted form of the text
# file will be saved as a separate file. Ben recommends using the replace()
# function in this exercise.

# importing modules and the onlyWords() function which splits lines into words
# only
import string
import sys

if len(sys.argv) == 1:
    print("No file specified.")
    quit()

try:
    # opening file to be read.
    with open(sys.argv[1]) as file:
        # opening file to write to.
        red_file_name = sys.argv[1].replace(".txt","") + "_redacted.txt"
        with open(red_file_name, "w") as red_file:

            for line in file:
                line_list = line.split() # simple split of read file line
                line_list_temp = line.upper().split() # split and caps of read file line for ref
                line_list_temp_mod = line_list_temp.copy() # split and caps of read file line to modify

                # opening sensitive words text file.
                with open("sensitive_words.txt") as sens_words:
                    for sens_word in sens_words: # Going through each word in sensitive words
                        sens_word = sens_word.rstrip("\n")
                        sens_word_temp = sens_word.upper() # making all caps copy of sens word
                        asteriks_count = len(sens_word) # making a string of asteriks same length as the word
                        asteriks = "*" * asteriks_count

                        for word in line_list_temp_mod: # Going through each word in caps split line
                            if sens_word_temp in word: # Updating modifiable list with redactions
                                index = line_list_temp_mod.index(word)
                                line_list_temp_mod[index] = word.replace(sens_word_temp, asteriks)


                    for i in range(len(line_list_temp)):
                        if line_list_temp[i] != line_list_temp_mod[i]: # If an element in the
                        # caps list is different to an element in the modified caps list the indicies
                        # that the asteriks occupy is recorded
                            red_number = 0
                            red_beg = True
                            red_start_i = 0
                            for char in line_list_temp_mod[i]:
                                if char == "*" and red_beg:
                                    red_start_i = line_list_temp_mod[i].index("*")
                                    red_beg = False
                                    red_number += 1
                                elif char == "*":
                                    red_number += 1
                            working_word = line_list.pop(i)
                            working_word_ins = working_word[:red_start_i] + "*" * red_number + working_word[red_start_i+red_number:]
                            line_list.insert(i,working_word_ins)

                    # writing modified line list into new file.
                    write_line = " ".join(line_list)
                    red_file.write(write_line)
                    red_file.write("\n")
except FileNotFoundError:
    print("filename is invalid.")
