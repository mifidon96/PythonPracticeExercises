# A prgram that calculates the mean average from a sample of value inputs from
# the user. 0 will be used as a sentinal value to indicate that there are no
# values to be entered. If 0 is enterd first then an error message will be
# displayed. #

print("Please enter a set of numbers to find an average. Enter 0 when you are done.")

# initialising an empty list for numbers and the enterd number value as an empty
# string
numbers = []
num = ""

# Adding new numbers to the set, breaking the loop if num == 0
while num != 0:
    num = float(input("Add to set: "))
    # Excluding the terminating character 0 from the number set
    if num != 0: numbers.append(num)

# Error message if first entry is 0, resulting in an empty list
if numbers == []:
    print("Please add numbers to the set.")
# Calculating and displaying the mean average
else:
    set_size = len(numbers)
    av = sum(numbers) / set_size
    print("Mean average is: %.2f" % av)
