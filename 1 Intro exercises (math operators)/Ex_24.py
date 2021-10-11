# Program that takes in an amount of time in days, min sand seconds and returns
# that amount of time in seconds

d = int(input("Please enter the number of whole days: "))
h = int(input("Please enter the number of hours: "))
m = int(input("Please enter the number of minutes: "))
s = int(input("Please enter the number of sconds: "))

s = s + m*60 + h*60*60 + d*24*60*60

print("That is %i seconds!" % s)
