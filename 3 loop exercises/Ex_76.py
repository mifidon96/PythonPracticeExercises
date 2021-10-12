# program that finds the prime factors of an integer ##

n = int(input("Enter an intger greater than 1: "))
if n < 2:
    print("This integer is not greater than 1.")
else:
    print("The prime factors of n are:")
    f = 2
    while f <= n:
        if n % f != 0:
            f += 1
        else:
            print(f)
            n = n // f
