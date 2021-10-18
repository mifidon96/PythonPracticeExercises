## A Program that reads every file in a data set of baby names for boys and
# girls between the years 1900 - 2012 and determines which names were most
# popular in at least one year. Each file contains the name and number of uses.
# Program will return two lists, one for boys and one for girls. Neither list
# should have repeated values. ##

# define a start and end year, go in and read each file for boys and girls,
# if name in in a dictionary then add to dictionary follwed by freq, update freq
# each time if name is found in net file, then use a max( key=lambda) to find the
# five most popular boys and girls names and put into lists then print.

import os

os.chdir(r"C:\Users\ijmes_000\Desktop\Compsci\Python practice\BS Workbook\BabyNames")

START_YEAR = int(input("Enter start year: "))
END_YEAR = int(input("Enter end year: "))


BoysGirls = ["Boys", "Girls"]

boy_dict = {}
girl_dict = {}

for year in range(START_YEAR, END_YEAR+1):
    for gender in BoysGirls:
        filename = str(year) + "_" + gender + "Names.txt"

        with open(filename) as f:
            for line in f:
                line = line.split()
                line[1] = int(line[1])
                if gender == "Boys":
                    if line[0] not in boy_dict:
                        boy_dict.update({line[0]:line[1]})
                    else:
                        boy_dict[line[0]] += line[1]
                else:
                    if line[0] not in girl_dict:
                        girl_dict.update({line[0]:line[1]})
                    else:
                        girl_dict[line[0]] += line[1]

top_ten_boy_list = sorted(boy_dict.items(), key=lambda item: item[1], reverse=True)[0:10]
top_ten_girl_list = sorted(girl_dict.items(), key=lambda item: item[1], reverse=True)[0:10]


print(f"\nTop 10 boys' names from {START_YEAR} to {END_YEAR}: {top_ten_boy_list}")
print(f"\nTop 10 girls' names from {START_YEAR} to {END_YEAR}: {top_ten_girl_list}")
