# Program that finds the geatest common divisor of two positive integers #

n = int(input("Enter a number: "))
m = int(input("Enter another number: "))

if n < m:
    d = n
else:
    d = m

while n % d != 0 or m % d != 0:
    d -= 1

print(d, "is the lowest common divisor.")
