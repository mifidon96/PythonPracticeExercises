## Program that determines the number of moles of gas in a given sample using
## ideal gas law

# Setting value of ideal gas constant
R = 8.314
# Taking input values of pressure, volume and temperature
P =  float(input("Please enter the system pressure in pascals:"))
V = float(input("Please enter the volume in litres: "))
T = 273.15 + float(input("Please enter the temperture in degrees C: "))

# Calculating using ideal gas law
n = (P*V)/(R*T)
# Display output
print("Number of moles of gas: %.2f" % n)
