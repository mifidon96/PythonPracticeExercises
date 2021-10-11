# A program that computes the body mass index (BMI) of an individual. Reading
# height and weight from user then use the BMI formula to calculate and display
# the result #

weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in meters: "))

BMI = weight/(height**2)

print("BMI calculated at: %.2f" % BMI)
