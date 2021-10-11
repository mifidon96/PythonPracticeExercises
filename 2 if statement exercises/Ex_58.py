# Programm that computes the day after the day specified. The brief specifies
# three seperate input statements. reusing code from Ex_57 to determine leap years.

day = int(input("Please input the day of the month: "))
month = int(input("Please input the month numerically: "))
year = int(input("Please input the year: "))

# checking if year is a leap year
if year % 400 == 0:
    leap = True
elif year % 100 == 0:
    leap = False
elif year % 4 ==0:
    leap = True
else:
    leap = False

# Setting number of days a month can have, accounting for feb in a leap year
# and generating calendar
d_30 = 31
d_31 = 32
if leap:
    d_feb = 30
else:
    d_feb = 29

Sep = Apr = Jun = Nov = list(range(1, d_30))
Jan = Mar = May = Jul = Aug = Oct = Dec = list(range(1, d_31))
Feb = list(range(1, d_feb))

calendar = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, oct, Nov, Dec]
# creating index values for month and days in the calendar
month_i = month - 1
# setting conditions for turn over of year, month and day. for year turnover,
# month and day will always be 01/01/year+1, for month turnover it will always be the
# 01/month+1/year and for day turnover simply day day+1/month/year. Also handles
# invalid dates (from 01/01/01 AD). Displays output message.
if month == 12 and day == len(calendar[month_i]):
    year += 1
    print("The next day is 01/01/%d" % year)
elif month < 12 and day == len(calendar[month_i]):
    month += 1
    print("The next day is 01/%02d/%d" % (month, year))
elif month <= 12 and day < len(calendar[month_i]):
    day += 1
    print("The next day is %02d/%02d/%d" % (day, month, year))
else:
    print("Please enter a valid date.")
