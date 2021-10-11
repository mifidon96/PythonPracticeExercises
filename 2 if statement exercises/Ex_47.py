# A program that asks the user to enter the month and day of birth then report
# the user's zodiac sign. ##

month = input("Please enter the month you were born (number): ")
day = input("Please enter the day of the month you were born: ")

age = int(day + month)

if 1222 <= age or age <= 119:
    zodiac = "Capricorn"
elif 120 <= age <= 218:
    zodiac = "Aquarius"
elif 219 <= age <= 320:
    zodiac = "Pisces"
elif 321 <= age <= 419:
    zodiac = "Aries"
elif 420 <= age <= 520:
    zodiac = "Taurus"
elif 521 <= age <= 620:
    zodiac = "Gemini"
elif 621 <= age <= 722:
    zodiac = "Cancer"
elif 723 <= age <= 822:
    zodiac = "Leo"
elif 823 <= age <= 922:
    zodiac = "Virgo"
elif 923 <= age <= 1022:
    zodiac = "Libra"
elif 1023 <= age <= 1121:
    zodiac = "Scorpio"
elif 1122 <= age <= 1221:
    zodiac = "Sagittarius"

print("You are a %s" % zodiac)
