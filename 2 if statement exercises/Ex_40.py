# A program that determines if a triangle is equilateral, isosceles, or scalene
# based on side length inputs by the user

# user input prompts
s1 = float(input("Enter the length of the first side of the triangle: "))
s2 = float(input("Enter the length of the second side of the triangle: "))
s3 = float(input("Enter the length of the third side of the triangle: "))

# list made of all side lengths
sides = [s1, s2 ,s3]
# If all lengths are equal then equilateral, all are different then scalene, and
# any other combination is isosceles as two must be equal by definition.
if s1 == s2 == s3:
    print("The triangle is equilateral!")
elif s1 != s2 != s3:
    print("The triangle is scalene!")
else:
    print("The triangle is isosceles!")
