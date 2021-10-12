## Program reads +ve and -ve integers and zeros from the user until a blank line
# is entered. The program will display the negative ingegers, followed by the
# zeros and the +ve integers but in the order that they were entered. ##

num = []
entry = input("Please enter an integer (blank to exit): ")
while entry != "":
    entry = int(entry)
    num.append(entry)
    entry = input("Please enter an integer (blank to exit): ")

numord = []
for i in num:
    if i < 0:
        numord.append(i)
for i in num:
    if i == 0:
        numord.append(i)
for i in num:
    if i > 0:
        numord.append(i)

print(num)
print(numord)
