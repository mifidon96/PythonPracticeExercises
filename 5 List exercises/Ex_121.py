## A function that determines the number of elements within a list that are
# >= some minimum value and < some maximum value. Parameters: the list, minimum
# value and maximum value . Returns: an integer result >= 0.
# main() program demonstrates function for several different lists. Ensuring
# function works for integers and floats. ##

def countRange(l,min,max):
    count = 0
    for e in l:
        if min <= e < max:
            count += 1
    return count


def main():
    list1 = [1, 2, 3, 5, 8, 9, 10, 13, 16, 17, 18, 18, 20]
    min, max = 10.0, 20.0
    print(countRange(list1, min, max))

    list2 = [0.3, 1.0, 4.7, 5.505, 6.0, 8.1, 9.01, 10.3, 14.0, 15.7, 18.7, 19.9, 20.0]
    min, max = 5, 19
    print(countRange(list2, min, max))

if __name__ == "__main__":
    main()
