# A function that simulates a bingo card. A five by five grid, with columns
# headed with the letters BINGO. five of 15 numbers can appear under each letter
# with B being 1 - 15, I being 16 - 30, etc.
# Another function that displays the card with proper formatting.
# main() program uses functions to create and display random bingo cards.
# Also make suitable for importing. #

def genBingoCard():

    from random import randint

    card = {"B":[],"I":[],"N":[],"G":[],"O":[]} # Initialising bingo card
    start = 1
    end = 15

    for letter in card:
        nums = []
        while len(nums) < 5:
            num = randint(start, end)
            if num not in nums:
                nums.append(num)
        card.update({letter:nums})
        start += 15
        end += 15

    return card

def displayBingoCard(card):

    print("   B   I   N   G   O") # printing headers

    index = 0
    for i in range(5): # printing out each number in each letter underneath the
    # corresponding letter in a column.
        for letter in card:
            print("%4d" % card[letter][index], end = "")
        print("\n")
        index += 1

def main():
    card = genBingoCard()
    displayBingoCard(card)

if __name__ == "__main__":
    main()
