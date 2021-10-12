## A program that converts between two number base systems. Supports all bases
# between and including binary and hexadecimal. A base outside this range will
# display an error and quit. ##

def baseconv(n, start_base, end_base):

    #### Setting up lists of characters to use for start and end bases ######

    import string
    char = string.digits + string.ascii_uppercase
    start_base_char = char[0:start_base]
    end_base_char = char[0:end_base]

    ############# Converting start base to a base 10 intermediate ############

    # Method is to read number from right to left, get the index of the
    # character being looked in the start_base_char list, then add this index
    # value * the character's position value to the value of the number;
    # n_value (expressed in base 10).
    pos_value = 1
    n_value = 0
    for i in range(len(n)-1,-1,-1):
        c_test = n[i]
        n_value += start_base_char.index(c_test) * pos_value
        pos_value *= start_base

    ######### Returning n_value as a string if desired end base is 10 #########
    if end_base == 10:
        return str(n_value)

    ########## Converting base 10 intermediate to new base notation #########
    else:
        # Initalising rsult to empty, position value exponent x to 0 and
        # n_value_test to use in calculation so as not to alter the var n_value.
        result = ""
        x = 0
        n_value_test = n_value

        # Method involves finding the higest value of x for
        # n_value_test // new_base**x != 0
        x = 0
        fits_in = 1
        while fits_in != 0:
            x += 1
            fits_in = n_value_test // end_base**x
        x -= 1

        # Then for each integer from highest value of x down to and including 0,
        # performing n_value test // new_base**x and
        # using this result as the index of the first character of the new
        # number as found in the list end_base_char, then inserting this as a
        # string into var result. Then n_value_test -= (new_base**x * index).
        for i in range(x,-1,-1):
            new_char_index = n_value_test // end_base**i # How many times pace holder goes into number
            result += str(end_base_char[new_char_index]) # Adding notation to result
            n_value_test -= new_char_index * end_base**i # updating number

        ### End of calculation and returning the car result containing a string ###
        return result

def main():
    start_base = int(input("Please enter the base (2-16) of the number to convert: "))
    n = input("Please enter the number to convert (in its base notation): ")
    end_base = int(input("Please enter the base (2-16) to convert the number into: "))

    if (2 <= start_base <= 16) and (2 <= end_base <= 16):
        new_number = baseconv(n, start_base, end_base)
        print("\n%s in base %d is equivalent to %s in base %d" %(n, start_base, new_number, end_base))
    else:
        print("\nEither the start or end base is out of the specified range (2-16).")
        exit()

if __name__ == "__main__":
    main()
