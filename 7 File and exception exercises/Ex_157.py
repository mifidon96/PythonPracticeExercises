## A program that records all baby names for boys and girls that were used in
# years 1900 - 2012 (entire data set).

import os

os.chdir(r"C:\Users\ijmes_000\Desktop\Compsci\Python practice\BS Workbook\BabyNames")

boy_names = []
girl_names = []
genders = ["Boys", "Girls"]

for year in range(1900, 2013):
    for gender in genders:
        filename = str(year) + "_" + gender + "Names.txt"
        with open(filename) as f:
            for line in f:
                line = line.split()
                if gender == "Boys" and line[0] not in boy_names:
                    boy_names.append(line[0])
                elif gender == "Girls" and line[0] not in girl_names:
                    girl_names.append(line[0])

print(f"Boys names: {boy_names}\n")
print(f"Girls names: {girl_names}")
