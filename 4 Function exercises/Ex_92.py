# A function that determines if a number is a prime, returning 'True' or 'False'.
# main() program will read integer from user and display output. #

def isPrime(n):
    n = int(n)
    prime = True
    # Logic is to make the divisor a floor division of the number being tested
    # by 2 (i.e. the largest number that could go into the tested number with
    # remainder 0) and then dividing it by every integer between it and 1. If
    # it returns a remainder 0 then it is not prime.
    if n > 1:
        d = n // 2
        while d != 1:
            if n % d == 0:
                prime = False
                d -= 1
            else:
                d -= 1
    else:
        prime = False
    return prime

def main():
    n = input("Please enter an integer: ")
    if isPrime(n):
        print("This number is a prime!")
    else:
        print("This number is not a prime.")

if __name__ == "__main__":
    main()
