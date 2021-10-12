# A function that determines if a list of values is sorted (either ascending
# or descending order)
# Parameter: a list of numbers. Returns: True or False.
# main() program reads numbers from the user and reports if list is sorted or
# not. #

def isSorted(list):
    ascending = False
    descending = False

    for i in range(len(list)-2):
        if list[i] < list[i+1]:
            ascending = True
        elif list[i] > list[i+1]:
            descending = True

    if ascending ^ descending:
        return True
    else:
        return False

def main():
    list = []
    entry = input("Enter a number (blank to quit): ")
    while entry != "":
        entry = float(entry)
        list.append(entry)
        entry = input("Enter a number (blank to quit): ")

    print(isSorted(list))

if __name__ == "__main__":
    main()
