
length = float(input("Please enter the length of the field in feet: "))
width = float(input("Please enter the width of the field in feet: "))
area_ft = length + width
area_ac = str(area_ft / 43560)

print("The area of the field is " + area_ac + "acres")
