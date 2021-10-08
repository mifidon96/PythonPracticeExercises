# converting from feet and inches to centimetres

# Taking input of number of feet and inches from user
feet = float(input("Please enter in the number of feet: "))
inches = float(input("And now inches:"))

# conversion factors
foot_to_inch = 12
inch_to_cm = 2.54

# converting values
feet_in_inches = feet * foot_to_inch
inches += feet_in_inches

cm = inches * inch_to_cm

# printing outputs
print("That is equivalent to %.2f cm" % cm)                     
