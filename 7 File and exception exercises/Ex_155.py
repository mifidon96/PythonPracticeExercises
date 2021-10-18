## Program That idntifies gender neutral names that were used in a specific year
# with an appropriate message if there are no gender nueutra names in that year.
# Error message if no data for the year specified.
import os

os.chdir(r"C:\Users\ijmes_000\Desktop\Compsci\Python practice\BS Workbook\BabyNames")

YEAR = input("Enter the year (1900 - 2012): ")

if YEAR == "":
    print("No year specified.")
    quit()
elif int(YEAR) > 2012 or int(YEAR) < 1900:
    print("No data available for year.")
    quit()

def openLoad(filename):
    with open(filename) as f:
        names = []
        for line in f:
            line = line.split()
            if line[0] not in names:
                names.append(line[0])
    return names

girl_filename = YEAR + "_GirlsNames.txt"
boy_filename = YEAR + "_BoysNames.txt"
girls_names = openLoad(girl_filename)
boys_names = openLoad(boy_filename)
gender_neutral = []

for name in girls_names:
    if name in boys_names:
        gender_neutral.append(name)

if len(gender_neutral) > 0:
    print(f"Gender netral names in {YEAR}: {gender_neutral}")
else:
    print("No gender neutral names.")
