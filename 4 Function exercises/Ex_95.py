## A function that generates a random liscence plate in either an old style
# (three letters followed by three numbers), or new (four numbers followed by
# three letters). main() function runs function and displays liscence plate.

def randLiscence():
    from random import randint
    liscence = ""
    isNew = randint(0,1)
    if isNew:
        for i in range(0,4):
            liscence += chr(randint(48,57))
        for i in range(0,3):
            liscence += chr(randint(65,90))
    else:
        for i in range(0,3):
            liscence += chr(randint(65,90))
        for i in range(0,3):
            liscence += chr(randint(48,57))
    return liscence

def main():
    print(randLiscence())

main()
