# A programme that reads the current time and date from the computer using
# the asctime function from the time module, and displays it to the user #

from time import asctime

time_now = asctime()
print("The time is:", time_now)
