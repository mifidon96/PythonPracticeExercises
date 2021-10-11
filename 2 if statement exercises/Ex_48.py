# A program that reads a year from th user and displays the animal associated
# with that year, can interpret any year from 0 AD onwards #

year = int(input("Please enter a year: "))

remainder = year % 12

if remainder == 0:
    animal = "Monkey"
elif remainder == 1:
    animal = "Rooster"
elif remainder == 2:
    animal = "Dog"
elif remainder == 3:
    animal = "Pig"
elif remainder == 4:
    animal = "Rat"
elif remainder == 5:
    animal = "Ox"
elif remainder == 6:
    animal = "Tiger"
elif remainder == 7:
    animal = "Hare"
elif remainder == 8:
    animal = "Dragon"
elif remainder == 9:
    animal = "Snake"
elif remainder == 10:
    animal = "Horse"
elif remainder == 11:
    animal = "Sheep"

print("That's the year of the %s!" % animal)
