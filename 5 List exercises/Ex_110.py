## An integer, n, is said to be perfect when the sum of all of the proper
# divisors of n is equal to n. For example, 28 is a perfect number because its
# proper divisors are 1, 2, 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28. A function
# that determines whether an intger is perfect. Parameter: an integer.
# Returns: True or False. main() program that uses the function to identify and
# display ll perfect numbers between 1 and 10,000. Importing function from
# Ex_109 ##

def isPerfect(n):
    from Ex_109 import properDivisor
    n = int(n)
    if n == sum(properDivisor(n)):
        return True
    else:
        return False

def main():
    list = []
    for i in range(1,10001):
        if isPerfect(i):
            list.append(i)
    print(list)

if __name__ == "__main__":
    main()
