## program that computes the parity bit for bytes of binary data entered by the
# user ###

#promting first byte from user and stting substring to count to "1"
byte = input("Input a byte of binary data (blank to end): ")
ones = "1"

# setting escape condition
while byte != "" and len(byte) == 8:
    # counting the number of "1" characters in string and checking if even or odd
    count = byte.count(ones)
    if count % 2 == 0:
        parity_bit = 0
    else:
        parity_bit = 1
    # Displaying output
    print("Even parity bit: %d" % parity_bit)
    # prompting next input / escape condition
    byte = input("Input a byte of binary data (blank to end): ")
else:
    print("Please only enter one byte (8 bits) of data.")
