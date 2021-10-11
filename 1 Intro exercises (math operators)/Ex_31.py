# Program reads a four-digit integer from the user and displays the sum of
# digits in the number, for example if the user enters 3141 your program should
# display = 9 #

number = input("Please enter a four digit number: ")

total = 0

for d in number:
    total += int(d)

print("Sum of the four digits in the number is:", total)
