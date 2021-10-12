## A function that checks for winning bingo cards. A crossed off number will be
# defined as the number 0, and a winning bingo card will have a line of five
# zeros, either vertical, horizontal or diagonal. Parameters: A dictionary
# simulating a bingo card. Returns: True or False (for a win).
# main() program will demonstrate function buy creating several bingo cards,
# displaying them and indicating whether or not they contain a winning line.
# at leaset one of which does not contain a winning line. ##


def bingoCheck(card):
    win = False

    # Vertical line check.
    for letter in card:
        if sum(card[letter]) == 0:
            win = True

    # horizontal line check
    if not win:
        index = 0
        while index < 5:
            count = 0
            for letter in card:
                count += card[letter][index]
            if count == 0:
                win = True
            index += 1

    # diagonal line check:
    if not win:
        index = 0
        tl_br = 0
        bl_tr = 0
        for letter in card: # first checking top-left to bottom-right
            tl_br += card[letter][index]
            index += 1
        index -= 1 # setting index to 4
        for letter in card: # then checking bottom left to top-right
            bl_tr += card[letter][index]
            index -= 1
        if tl_br == 0 or bl_tr == 0:
            win = True

    return win

def main():
    from Ex_138 import genBingoCard
    from Ex_138 import displayBingoCard
    from random import randint

    # Test a vertical win
    vert_win = genBingoCard()
    bingo = "BINGO"
    letter = bingo[randint(0,4)]
    vert_win.update({letter:[0,0,0,0,0]})
    print(bingoCheck(vert_win))
    displayBingoCard(vert_win)

    # Test a horizontal win
    horz_win = genBingoCard()
    index = randint(0,4)
    for letter in horz_win:
        horz_win[letter][index] = 0
    print(bingoCheck(horz_win))
    displayBingoCard(horz_win)

    # Test a diagonal win
    diag_win = genBingoCard()
    tl_br = 0
    bl_tr = 0
    choice = randint(0,1)
    if choice == 0:
        index = 0
        for letter in diag_win:
            diag_win[letter][index] = 0
            index += 1
    else:
        index = 4
        for letter in diag_win:
            diag_win[letter][index] = 0
            index -= 1
    print(bingoCheck(diag_win))
    displayBingoCard(diag_win)

    # Test a no win
    no_win = genBingoCard()
    print(bingoCheck(no_win))
    displayBingoCard(no_win)

if __name__ == "__main__":
    main()
