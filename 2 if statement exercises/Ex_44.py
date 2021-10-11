# Write a program that reads a month and day from the user. If the month and
# day match one of the three Canadian national holidays, New Year's day (Jan 1)
# Canada day (July 1), and Christmas day (Dec 25), then the program will display
# the holiday name. Otherwise stating that the day does not correspond to one
# of these days. #

date = input("Please input the date in the form dd/mm: ")

if date == "01/01":
    print("It is New Year's day!")
elif date == "01/07":
    print("It is Canada day!")
elif date == ("25/12"):
    print("It is Christmas day!")
else:
    print("It is not a public holiday.")
