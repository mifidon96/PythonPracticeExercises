## A function that that creates a new copy of a list with data outliers
# (anomalous experimental data) removed. Parameters: a list, a +ve integer (n).
# Returns: a copy of the list with the n largest and n smallest element values
# removed. order of elements does not have to match that of original list.
# main() program to demonstrate function: displays list and after and before.
# error message if list has less than 4 elements ##

def removAnom(list,n):
    list.sort()

    for i in range(n):
        del list[0]
        del list[len(list)-1]

    return list


def main():
    list = []
    entry = int(input("Please enter an integer to add to list (0 to exit): "))

    while entry != 0:
        list.append(entry)
        entry = int(input("Please enter an integer to add to list (0 to exit): "))

    if len(list) < 4:
        print("List size is too small.")
        quit()

    n = int(input("Please enter the number of outliers to remove either side of data set about the median: "))
    print(list)
    print(removAnom(list,n))

if __name__ == "__main__":
    main()
