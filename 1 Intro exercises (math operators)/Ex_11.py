# Programme to convert from miles per US gallon to Litres per 100 Km

# Take input from the user

MPG = float(input("Please enter a value in miles per gallon: "))

# converting from MPG to KmPG, as mile to Km ratio is 1:1.60934
kmPG = MPG * 1.160934
# converting from kmPG to km/L, as US gallon to litre ratio is 1:3.78541
kmPL = kmPG/3.78541
# converting from kmPL to L/100km
conv = 1.00/kmPL
LP100KM = conv * 100
#Printing result
print('%.4g' % LP100km)
