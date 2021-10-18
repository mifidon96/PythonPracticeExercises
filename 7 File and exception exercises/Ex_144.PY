## A program that will read lines from a file, and write these lines to a new
# file with each line beginning with a line number. ##

file_r = input("Enter a file to add line numbers to: ")

file_w = input("Enter the name of the new file: ")

with open(file_r) as f_r:
    with open(file_w, "w") as f_w:
        line_num = 1
        for line in f_r:
            entry = f"{line_num}: {line}"
            print(entry, file=f_w)
            line_num += 1
