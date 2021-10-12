## A program that converts decimal to binary from a user input. Algorithm is
# provided ##

# user input prompt
num_dec = int(input("Please input an integer: "))

# setting updateable variable to work with integer in decimal notation and
# initialising result output as an empty string
q = num_dec
result = ""

# Loop for converting decimal to binary, 'if' statement is to accomodate for a
# 0 entry.
if q != 0:
    while q != 0:
        r = q % 2
        result = str(r) + result
        q = q // 2
else:
    result = 0


# Displaying output to user
print(num_dec,", in binary is:", result)
