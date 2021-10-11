# Program that converts a number of seconds into D:HH:MM:SS format

s_in_day = 60 * 60 * 24
s_in_hour = 60 * 60
s_in_min = 60

s = int(input("Please input a number of seconds: "))

d = s // s_in_day
s = s % s_in_day

h = s // s_in_hour
s = s % s_in_hour

m = s // s_in_min
s = s % s_in_min

print("That is the same as %d : %02d : %02d : %02d" % (d,h,m,s))
