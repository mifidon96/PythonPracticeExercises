# A program that reads a erathquake magnitude (richter) from the user and
# displays the appropriate descriptor ##

mag = float(input("Please input a magnitue value (Richter): "))

if mag < 2.0:
    desc = "Micro"
elif 2.0 <= mag < 3.0:
    desc = "Very minor"
elif 3.0 <= mag < 4.0:
    desc = "Minor"
elif 4.0 <= mag < 5.0:
    desc = "Light"
elif 5.0 <= mag < 6.0:
    desc = "Moderate"
elif 6.0 <= mag < 7.0:
    desc = "Strong"
elif 7.0 <= mag < 8.0:
    desc = "Major"
elif 8.0 <= mag < 10.0:
    desc = "Great"
else:
    desc = "Meteoric"

print("This magnitude is described as a %s Earthquake" % desc)
