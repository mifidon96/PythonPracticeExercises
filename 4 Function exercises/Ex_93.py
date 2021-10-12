## A funcion that returns the next prime number larger than some integer n,
# n is the only parameter. The function will use the imported function,
# isprime() from Ex_92. ##

def nextPrime(n):
    from Ex_92 import isPrime
    t = int(n)
    t += 1
    while isPrime(t) == False:
        t += 1
    return t

def main():
    n = input("Please enter an integer to find the next prime up: ")
    next_prime = nextPrime(n)
    print("The next prime up is:", next_prime)

main()
