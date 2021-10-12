## A function that generates a deck of cards using two character notation.
# No parameters and returns a list of cards. Another function that randomly
# shuffles the deck, Must write own loop and nt use a Python shuffle function.
# main program displays the deck of cards before and after shuffling. Make file
# suitable for functions to be imported ##


def createDeck():
    suits = "shcd"
    face_ace = "JQKA"
    deck = []
    for s in suits:
        for n in range(2,11): # Add numbers
            n = str(n)
            c = n + s
            deck.append(c)
        for f in face_ace: # face cards and ace
            c = f + s
            deck.append(c)
    return deck

def shuffle(deck):
    from random import randint
    for i in range(100000):
        take_i = randint(0,51)
        put_i = randint(0,51)
        card = deck.pop(take_i)
        deck.insert(put_i, card)
    shuffled_deck = deck
    return shuffled_deck

def main():
    deck = createDeck()
    print("Deck:\n", deck)
    shuffled_deck = shuffle(deck)
    print("Shuffled deck:\n", shuffled_deck)

if __name__ == "__main__":
    main()
