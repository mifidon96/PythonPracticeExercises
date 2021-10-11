# A program that displays the number of days in a month provided by the user.

month = input("Please enter a month: ")

month_thirty = ["September", "April", "June", "November"]
month_thirty_one = ["January", "March", "May", "July", "August", "October", "December"]
exception = "February"

if month in month_thirty:
    print("This month has thirty days.")
elif month in month_thirty_one:
    print( "This month has thirty one days.")
elif month == exception:
    print("This month has 28 and 29 days (on a leap year).")
else:
    print("The month you entered isn't valid.")
