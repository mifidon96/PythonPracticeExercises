## A function that turns a number between 0 and 999 into english
# e.g. 142 returns "one hundred forty two" (N American spelling). main() Program
# reads number from the user and displays output.

def num2word(num):
    singles = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
    8:"eight", 9:"nine", 0:""}
    teens = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen",
    15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
    tens = {20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy",
    80:"eighty", 90:"ninety"}

    amount = ""

    if num // 100 != 0:
        amount += singles[num // 100] + " hundred "
        num %= 100

    if num // 10 >= 2:
        amount += tens[(num // 10)*10] + " "
        num %= 10

    if num in teens:
        amount += teens[num]
    elif num in singles:
        amount += singles[num]

    return amount

def main():
    from random import randint
    for i in range(10):
        num = randint(1,999)
        print(num, ":", num2word(num))
    #num = int(input("Please enter a number between 1 and 999: "))

    #print(num2word(num))

if __name__ == "__main__":
    main()
