## Program that generates a random selection of numbers between 1 and 49 for a
# lottery ticket. Ensure the number has no duplicates. Display number in
# ascending order. ##

from random import randint
ticket = []

while len(ticket) < 6:
    num = randint(1,49)
    if num not in ticket:
        ticket.append(num)

ticket.sort()

print(ticket)
