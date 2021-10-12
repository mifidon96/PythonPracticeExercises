# A function that returns a list containing every possible sublist of a list
# For example, the sublists of [1, 2, 3] are [], [1], [2], [3], [1, 2],
# [2, 3] and [1, 2, 3].##


def allSublists(list):
    SUBLISTS = [[]]

    # Initialising the length of the sublists we want to look for
    length_sublist = 1
    # defining biggest list as itself
    while length_sublist <= len(list):
        # Initialising index of the start element of sublist
        element_index = 0
        # Ensuring sublist does not exceed the length of the input list
        while element_index + length_sublist <= len(list):
            # Appending the sublist as a slice and incrementing the index of
            # the start element of sublist
            sublist_insert = list[element_index:element_index+length_sublist] # end index my not work if out of range
            SUBLISTS.append(sublist_insert)
            element_index += 1
        # Incrementing the length of the sublist to look for
        length_sublist += 1

    print(f"Sublists in {list}:\n")
    for sublist in SUBLISTS:
        print(sublist)

def main():
    list = [1,2,3,4,5,6,7,8,9,10]
    allSublists(list)

if __name__ == "__main__":
    main()
