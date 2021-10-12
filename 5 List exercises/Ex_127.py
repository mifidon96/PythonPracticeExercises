## Program that uses the 'Sieve of Eratosthenes' method to find prime numbers.
# in a given range. It involves crossing out numbers in a numberline from 0 to
# the limit of the range however it relies on the numbers simply being crossed
# out on a piece of paper and not disappearing from the list alltoghether.
# To simulate this you simply replace the element with a 0 value.
# if algrithm is correectly implements it should display answer in less than a
# few seconds. ##

limit = int(input("Please enter a number to set as the range limit: "))

# creating list of usble samples
sample = []
for i in range(2,limit+1):
    sample.append(i)

for p in sample:
    if p != 0:
        for i in range(2*p-2,limit-1,p):
            sample[i] = 0


# taking non-zero elements of sample and appending to prime list.
primes = []
for n in sample:
    if n != 0:
        primes.append(n)
# Displaying primes.
print("Primes:", primes)
