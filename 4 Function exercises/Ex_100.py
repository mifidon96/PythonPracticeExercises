## Function that determines how many days there are in a particular
# month. Parameters: month as an integer, year as four-digit integer
# account for leap days in feb. Returns: number of days.
# main() function reads input and displays output ##

def dayAmount(month, year):
    # Determining if leap year
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 ==0:
        leap = True
    else:
        leap = False

    # lists of months with thirty/ thirty one days
    thirty_days = [4,6,9,11]
    thirty_one_days= [1,3,5,7,8,10,12]

    # Returning days in the month of each year.
    if month in thirty_days:
        return 30
    elif month in thirty_one_days:
        return 31
    elif leap:
        return 29
    else:
        return 28

def main():
    month = int(input("Enter the month as an integer value: "))
    year = int(input("Enter the year: "))
    days = dayAmount(month,year)
    print("Number of days in this month of %d is %d" % (year, days))

if __name__ == "__main__":
    main()
