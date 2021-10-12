## A proper divisor of a positive integer, n, is a positive integer less than n
# which divides evenly into n. A function that computes all proper divisors of
# a positive integer, Parameter: positive function. Returns: a list of all
# proper divisors. main() program to demonstrate the function, only runs when
# not imported. ##

def properDivisor(n):
    divisors = []
    for i in range(1,n):
        if n % i == 0:
            divisors.append(i)

    return divisors

def main():
    n = int(input("Please enter a positive integer: "))

    list = properDivisor(n)
    print("Proper divisors of %d:" % n)
    print(list)

if __name__ == "__main__":
    main()
