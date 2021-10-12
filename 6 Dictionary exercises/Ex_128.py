## A function that finds all of the keys in a dictionary that map to a certain
# value. Parameters: dictionary and the value to search keys for. Returns:
# a (possibly empty) list of keys. Function suitable for import.
# main() program demonstrates the function. ##

def reverseLookup(dict, val):
    keys = []

    for key, value in dict.items():
        if value == val:
            keys.append(key)

    return keys


def main():
    ages = {"John": 21, "Adam": 23, "Alex": 21, "Jack": 22, "Frank": 21}
    age = 21
    print(reverseLookup(ages, age))

if __name__ == "__main__":
    main()
