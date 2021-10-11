### Program that takes three untegers from user and returns them in order

n1 = int(input("Please input the first integer: "))
n2 = int(input("Please input the second integer: "))
n3 = int(input("Please input the third integer: "))

small = min(n1, n2, n3)
large = max(n1, n2, n3)
middle = n1 + n2 + n3 - small - large

print(small, middle, large)
