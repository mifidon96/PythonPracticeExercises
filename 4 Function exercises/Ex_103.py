## A function that determines if a date is 'magic',
# i.e. if the day * month == last two digits of the year.
# e.g. (June 10, 1960 is magic bc 6 * 10 = 60)
# main() program will use the function to find all the magic dates in the 20th
# century. ##

def isMagic(d,m,y):
    # initialising magic to False

    magic = False
    # Obtaining last two numbers of the year
    y_det = str(y)
    y_det = y_det[len(y_det)-2:]
    y_det = int(y_det)

    # Checking if magic
    if d * m == y_det:
        magic = True

    return magic

def main():
    # Importing function that returns number of days in a month of a specific year
    from Ex_100 import dayAmount

    # looping through every year of the 20th century, and every month in that
    # year, generating the number of days and looping through those. Using the
    # year, month and day numbers as parameters for the isMagic() function.
    # if isMagic == true then displaying the date.
    for y in range(1900,2000):
        for m in range(1,13):
            number_of_d = dayAmount(m,y)
            for d in range (1,number_of_d+1):
                if isMagic(d,m,y):
                    print("%02d/%02d/%d" % (d,m,y))

if __name__ == "__main__":
    main()
