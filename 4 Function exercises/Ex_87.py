## A function that takes a string and the width of the terminal as its two
# parameters, snd returns the same string but centers in the terminal window.
# Only leading spaces are permitted, no extra characters on end of the string ##

def strcent(string, width):
    # Calculating the index of the position Left of the Centre of the terminal
    LoC = width // 2
    LoC_i = LoC - 1
    # Calculating the size of half of the string and then the index of the Letter
    # Left of the Centre of the string
    half_string_size = len(string) // 2
    LLoC_i = half_string_size - 1
    # Calculating the number of spaces needed to shift the letter
    shift = LoC_i - LLoC_i
    # Shifting string and creating display
    space = " "
    display = shift * space + string
    print(display)

def main():
    string = input("Plese enter a string to be centered: ")
    width = int(input("Please enter the width of the terminal: "))
    strcent(string,width)

main()
