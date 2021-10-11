# A program that begins by reading a temperature form the user in degrees C,
# then displays the equivalent temperature in Farenheit and Kelvin #

temp_C = int(input("Enter a temperature in degrees Celcius: "))

temp_F = temp_C * (9/5) + 32
temp_K = temp_C + 273.15

print("The temperature in Farenheit is: %.2f K \nThe temperature in Kelvin is %.2f F" % (temp_F, temp_K))
