# Program that converts between celcius and faranheit #

# generating list of numbers, 0 to 100 in steps of ten
celc = list(range(0,101,10))

for C in celc:
    F = C * (9/5) + 32
    print("%.2f C is equivalent to %.2f F" % (C, F))
