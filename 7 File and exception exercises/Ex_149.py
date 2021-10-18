## A program that convers from letter grades to grade points and vice versa.
# Will work by attempting to convert each value entered as a number to letter
# grade. If an exceptin occurs then program will try a conversion from letter
# to number of grade points. If both conversions fail then an error message
# will be displayed. Will continue conversions until a blank line. ##

grade_list = [0, 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0]

num_to_letter = {4.0:"A+ or A", 3.7:"A-", 3.3:"B+", 3.0:"B", 2.7:"B-", 2.3:"C+",
2.0:"C", 1.7:"C-", 1.3:"D+", 1.0:"D", 0:"F"}

letter_to_num = {"A+":4.0, "A":4.0, "A-":3.7, "B+":3.3, "B":3.0, "B-":2.7, "C+":2.3,
"C":2.0, "C-":1.7, "D+":1.3, "D":1.0, "F":0}

entry = input("Enter a number or letter grade to convert: ")
while entry != "":
    entry = entry.upper()

    try: # Converting number grade to letter.
        entry = float(entry)
        if entry in num_to_letter: # Direct match
            letter_grade = num_to_letter[entry]

        else: # Looking to round
            if grade_list[0] < entry < grade_list[-1]: # Checking if in range
                for i in range(len(grade_list)-1):
                    if grade_list[i] < entry < grade_list[i+1]:
                        med = (grade_list[i] + grade_list[i+1])/2
                        if entry >= med:
                            letter_grade = num_to_letter[grade_list[i+1]]
                        else:
                            letter_grade = num_to_letter[grade_list[i]]
            else: # Display if number is out of range
                letter_grade = False
                print("Number is out of range.")

        if letter_grade: # Display
            print(f"Letter grade is {letter_grade}")


    except ValueError: # Checking to see if entry is a letter grade
        if entry in letter_to_num:
            num_grade = letter_to_num[entry]
            print(f"Number grade is {num_grade}")
        else:
            print("This is not a valid input")

    entry = input("Enter a number or letter grade to convert: ")
