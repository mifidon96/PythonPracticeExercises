## Program that takes a date from the user and returns what season it is in ##

#prompting user input for month and day
month = input("Please enter the month: ")
day = int(input("Please enter the day: "))

# Setting conditions for months that lie wholly in a season
if month == "January" or month == "February":
    season = "Winter"
elif month == "April" or month == "May":
    season = "Spring"
elif month == "July" or month == "August":
    season = "Summer"
elif month == "October" or month == "November":
    season = "Autumn"
# Setting conditions for transition months
if month == "March" and day >= 20:
    season = "Spring"
elif month == "March":
    season = "Winter"

if month == "June" and day >= 21:
    season = "Summer"
elif month == "June":
    season = "Spring"

if month == "September" and day >= 22:
    season = "Autumn"
elif month == "September":
    season = "Summer"

if month == "December" and day >= 21:
    season = "Winter"
elif month == "December":
    season = "Autumn"
# displaying output
print("%s %d is in %s" % (month, day, season))
