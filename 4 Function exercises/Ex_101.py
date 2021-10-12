## A functioon that takes in a numerator and denominator of a fraction,
# determines the reduced form of the fraction and returns this.
# Parameters: two integers. Returns: two integers
# main() programme reads and displays user input and output. ##

def fractRed(numer,denom):
    if numer < denom:
        d = numer
    else:
        d = denom

    while numer % d != 0 or denom % d != 0:
        d -= 1

    new_numer = numer / d
    new_denom = denom / d

    return new_numer, new_denom

def main():
    numer = int(input("Please enter the numerator: "))
    denom = int(input("Please enter the denominator: "))
    reduced_fract = fractRed(numer, denom)
    print("Reduced fraction is: %d/%d" % reduced_fract)


if __name__ == "__main__":
    main()
