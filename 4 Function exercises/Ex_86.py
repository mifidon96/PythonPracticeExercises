## Program that displays the complete lyrics to the 'Twelve Days of Christmas'.
# Uses a function that takes the verse number as its only parameter and displays
# the relevant verse. Also uses an imprt of the function from Ex_85.

def verse(vn):
    # Converting parameter to an integer
    vn = int(vn)
    # Intro for each verse, using the ordinal function
    from Ex_85 import ord
    ordinal = ord(vn)
    intro = ("On the %s day of Christmas \nmy true love gave to me:" % ordinal.lower())

    # Body of verse
    # Writing out the lines for each verse
    v_1_ex = "A partridge in a pear tree."
    v_1 = "And a partridge in a pear tree."
    v_2 = "Two turtle doves,"
    v_3 = "Three french hens,"
    v_4 = "Four calling birds,"
    v_5 = "FIVE GOOOOOLD RIIIIIIINGS!!!"
    v_6 = "Six geese a' laying,"
    v_7 = "Seven swans a' swimming,"
    v_8 = "Eight maids are milking,"
    v_9 = "Nine ladies dancing,"
    v_10 = "Ten lords a' leaping,"
    v_11 = "Eleven pipers piping,"
    v_12 = "Twelve drummers drumming,"

    # Creating a list of verses with the first verse exeption at index 0
    verses = [v_1_ex, v_1, v_2, v_3, v_4, v_5, v_6, v_7, v_8, v_9, v_10, v_11, v_12]

    if vn == 1:
        print("%s\n%s\n" % (intro, v_1_ex))
    else:
        print(intro)
        for i in range(vn,0,-1):
            print(verses[i])
        print("\n")

def main():
    for i in range(1,13):
        verse(i)

main()
