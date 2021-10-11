# A program that determines if a year is a leap year #
# propmting user input
year = float(input("Please enter a year to find out if it is a leap year: "))
# Checking leap year conditions
if year % 400 == 0:
    leap = True
elif year % 100 == 0:
    leap = False
elif year % 4 ==0:
    leap = True
else:
    leap = False
# printing correct input
if leap:
    print("%.0f is a leap year" % year)
else:
    print("%.0f is not a leap year" % year)
