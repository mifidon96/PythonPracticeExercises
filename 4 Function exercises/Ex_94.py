## A function that generates a random password. Password should be between
# 7 - 10 characters long, each character a random selection from positions 33 -
# 126 in the ASCII table. No parameters needed, returns the random password.
# main() will display the password and will not run if imported. ##

def randPass():
    from random import randint
    password = ""

    length = randint(7,10)
    for i in range(0,length):
        char = chr(randint(33,126))
        password += char

    return password

def main():
    print(randPass())

if __name__ == "__main__":
    main()
