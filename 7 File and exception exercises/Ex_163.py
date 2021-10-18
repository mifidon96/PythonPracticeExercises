## A prgram that searches a file to find words that contain each of the five
# vowels, a, e, i, o, u, and y (semi vowel) exactly once and in order. User will
# provide the name of the file. Display error message if file input is invalid
# or something goes wrong while searching for words. ##

filename = input("Please specify a file: ")

m_letters = ["A", "E", "I", "O", "U", "Y"]
magic_words = []

try:
    with open(filename) as file:
        for line in file:
            # Remving case sensitivity and splitting line into individual words.
            line = line.upper()
            line_list = line.split()

            # Going through each word in the line
            for word in line_list:
                forbidden_letters = []
                i_m = 0
                max = len(word)

                for i_w in range(max):
                    if word[i_w] in forbidden_letters:
                        break
                    if word[i_w] == m_letters[i_m] and word[i_w] not in forbidden_letters:
                        forbidden_letters.append(m_letters[i_m])
                        i_m += 1
                    # If we have made our way through all the magic letters
                    # we have a magic word!
                    if i_m == len(m_letters):
                        magic_words.append(word)

        # Displaying magic words
        if len(magic_words) > 0:
            print("\nMagic words found in this file:")
            for magic_word in magic_words:
                print(magic_word)
        else:
            print("No magic words were found.")

except FileNotFoundError:
    print("Invalid file input.")
