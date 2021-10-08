from math import *
a = float(input("Input first integer: "))
b = float(input("Input second integer: "))

sum = a + b
b_from_a = a - b
prod = a*b
quot = a/b
rem = a % b
loga = log10(a)
ind = a**b

print("\nSum: %.3f" %sum)
print("Difference: %.3f" %b_from_a)
print("Product: %.3f" %prod)
print("Quotient: %.3f" %quot)
print("Remainder: %.3f" %rem)
print("Log(a): %.3f" %loga)
print("Raised to power: %.3f" %ind)
      
