# Programme that generates an 8x8 chess board and given a co-ordinate value
# form the user will report if a square is black or white. ##

# creating game board (axis lists)
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Prompting user input
square = input("Please enter a co-ordinate in the form of a letter and a number: ")
# Separating input string into two values, a string for the letter and integer
# for the number
letter = square[0]
number = int(square[1:])
# Checking to see if the co-ordinate entered is valid i.e exists on the board
if letter in letters and number in numbers:
    # getting the indecies of the letter and number values in axis lists
    letter_i = letters.index(letter)
    number_i = numbers.index(number)
    # Addition of both axis element indices will be a black square if the sum is
    # an even number, or a white if it is odd. This evalueates that and assigns coulour
    if (letter_i + number_i) % 2 == 0:
        colour = "black."
    else:
        colour = "white."
    print("This square is", colour)
# Print statement for when a non-existnt co-ordinate is entered.
else:
    print("Sorry, but the co-ordinate that you entered does not exist on this board")
