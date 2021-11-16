## A recursive function that determines wheter or not it is possible to
# construct a particular total using a specific number of coins. e.g. can you
# have a total of $1.00 using four coins? Yes, if each coin is a quarter,
# however you cannot have $1.00 using five coins. Read input from the user and
# display a message indicating whether or not it is possible. ##

class State:
    def __init__(self, total, n_coins):
        self.n_coins = n_coins
        self.total = total
        self.coins = [0.25, 0.1, 0.05, 0.01]

    def recur(self):
        if self.total > 0 and self.n_coins > 0:
            for coin in self.coins:
                i = State(self.total-coin, self.n_coins-1)
                # print("\ntotal:", self.total)
                # print("n_coins:", self.n_coins)
                # print("coin:", coin)
                answer = False or i.recur()
                if answer:
                    return True
        elif self.total == 0 and self.n_coins == 0:
            # print("\ntotal:", self.total)
            # print("n_coins:", self.n_coins)
            return True
        elif self.total < 0 or self.n_coins < 0:
            return False

def main():
    total = float(input("Please enter an amount in $CAD: "))
    n_coins = int(input("Please enter an amount of coins to make the total: "))
    start = State(total, n_coins)
    answer = start.recur()
    if answer:
        print("Yes!")
    else:
        print("No!")

if __name__ == "__main__":
    main()
