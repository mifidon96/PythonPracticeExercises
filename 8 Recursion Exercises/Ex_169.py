## A recursive function that computes the edit difference (how many changes
# would be needed to convert one word into another e.g. letter substitutions,
# insertions or deletions) between two strings. The algorithm is provided for
# this challenge. ##

def editDiff(s, t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0
        if s[-1] != t[-1]:
            cost = 1
        d1 = editDiff(s[:len(s)-1], t) + 1
        d2 = editDiff(s, t[:len(t)-1]) + 1
        d3 = editDiff(s[:len(s)-1], t[:len(t)-1]) + cost
        return min(d1, d2, d3)

def main():
    s = input("Please enter a word: ")
    t = input("Please enter another word: ")
    print(f"The edit difference is {editDiff(s, t)}")

if __name__ == "__main__":
    main()
