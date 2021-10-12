## A function that deals players a hand of cards. function should modify the deck,
# removing the card as it is dealt to a hand, and cards should be dealt one at
# a time to each hand as is customary. Parameters: number of hands,
# cards per hand, and the deck of cards. Return: a list containing all the hands
# that were dealt with each elemnt being a list of cards.
# main() program that creates, shuffles and deals a deck of cards. Display the
# hands along with the remaining cards in the deck. ##

def deal(n_h, n_c, deck):
    # constructing a list of lists (number of empty hands)
    hands = []
    for i in range(n_h):
        hand = []
        hands.append(hand)

    for i in range(n_c): # dealing cards giving one cards to each player one at a time
        for hand in hands:
            card = deck.pop(0)
            hand.append(card)

    return hands

def main():
    from Ex_118 import createDeck
    from Ex_118 import shuffle

    deck = shuffle(createDeck())
    n_h = int(input("Please enter the number of hands: "))
    n_c = int(input("Please enter the number of cards per hand: "))

    hands = deal(n_h, n_c, deck)
    print(hands, "\n")
    print(deck)

if __name__ == "__main__":
    main()
