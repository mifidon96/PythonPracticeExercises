## A function that finds an approximation of a square root using recursion.
# A main() program will demonstrate the function for a set of numbers. ##

# The algorithm used in Ex_71 but implementing recursion insted of iteration.
def sqRoot(n, guess = 1.0):
    if n-(10**-12) < guess**2 < n+(10**-12):
        return guess
    else:
        guess = (guess+(n/guess))/2
        return sqRoot(n, guess)

def main():
    n = float(input("Please enter a number: "))
    print(sqRoot(n))

if __name__ == "__main__":
    main()
