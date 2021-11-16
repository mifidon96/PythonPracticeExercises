## A program that converts decimal numbers to binary. For all other positive
# integers, n, compute the next digit and make a recursive call. Output of
# function is a string containing the number in binary notation. Display error
# if ingeter provided by user is negative ##

def dec2bin(n):
    # Entry by user will be an integer, on completion of the function, n will be
    # converted to a float. This allows an entry of 0 by the user to return "0".
    if n == 0 and type(n) == int:
        return "0"
    if n > 0:
        r = n % 2
        n = n // 2
        n = float(n)
        return dec2bin(n) + str(int(r))
    else:
        return ""

def main():
    n = int(input("Input a positive integer to convert to binary: "))
    if n >= 0:
        print(dec2bin(n))
    # elif n == 0:
    #     print(str(0))
    else:
        print("This is not a positive integer.")
        quit()

if __name__ == "__main__":
    main()
