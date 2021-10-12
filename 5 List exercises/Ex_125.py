## A function that determines if a list is a sublist of another. e.g.
# [1], [2], [3], [4] are all sublists of [1, 2, 3, 4].
# [2, 4] is not a sublist because the elements are not adjacent in the list.
# An empty list is a sublist of any list and also of itself.
# [1, 2, 3, 4] is also a sublist of [1, 2, 3, 4].
# Function takes two arguments, a smaller list and a larger list. Function
# returns True or False. ##

def isSublist(larger, smaller):
    if smaller == []:
        return True
    elif larger == smaller:
        return True

    else:
        answer = True
        if smaller[0] in larger:
            i = larger.index(smaller[0])
            for element in smaller:
                if i < len(larger) and element == larger[i]:
                    i += 1
                else:
                    answer = False
            return answer
        else:
            return False

def main():
    larger = [1, 2, 3, 4]
    smaller = [1]
    print(isSublist(larger, smaller)) # TRUE
    larger = [1, 2, 3, 4]
    smaller = [2]
    print(isSublist(larger, smaller)) # TRUE
    larger = [1, 2, 3, 4]
    smaller = [5]
    print(isSublist(larger, smaller)) # FALSE
    larger = [1, 2, 3, 4]
    smaller = [2,3]
    print(isSublist(larger, smaller)) # TRUE
    larger = [1, 2, 3, 4]
    smaller = [4,5]
    print(isSublist(larger, smaller)) # FALSE
    larger = [1, 2, 3, 4]
    smaller = [1, 2, 3, 4]
    print(isSublist(larger, smaller)) # TRUE
    larger = [1, 2, 3, 4]
    smaller = []
    print(isSublist(larger, smaller)) # TRUE

if __name__ == "__main__":
    main()
