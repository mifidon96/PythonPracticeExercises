## program that reads canadian postal codes from the user and displays the
# province (first letter) and weather it is rural or urban (0 or otherwise resp.)
# Error message if code begins with an invalid character. ##

provinces = {"Newfoundland":"A", "Nonva Scotia":"B", "Prince Edward Island":"C",
 "New Brunswick":"E", "Quebec":["G", "H", "I"],
 "Ontario":["K", "L", "M", "N", "P"], "Manitoba":"R", "Saskatchewan":"S",
 "Alberta":"T", "British Colombia":"V", "Nunavut":"X",
 "/Northwest Territories":"X", "Yukon":"Y"}

correct = False
zip_code = input("Please enter a Canadian postal code: ")
location = ""

if zip_code[1] == 0:
    location += "A rural area in "
else:
    location += "An urban area in "

for province, letter in provinces.items():
    if zip_code[0] in letter:
        location += province
        correct = True
location += "."

if not correct:
    print("This is not a valid postal code.")
else:
    print(location)
