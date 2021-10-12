## Prgram that caluculates the grade point average from a set of entered grades.
# The brief says not to worry about error checks (assume user will enter the
# correct letters) ##

# Creating list of letter grades and corresponding GPA scores at same index
grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
GPAs = [4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0]
# intitlizing counter n and running total = 0
n = 0
total = 0
# prompting first user input
entry = input("Please enter letter grade (blank to end): ")
# defining escape conditon for while loop
while entry != "":
    # retreiving GPA score for enterd letter grade
    GPA = GPAs[grades.index(entry)]
    # Adding GPA for entered grade to running total
    total += GPA
    # Adding one to counter
    n += 1
    # # prompting next entry / escape line
    entry = input("Please enter letter grade (blank to end): ")
# calculating average with running total and counter
final_GPA = total / n
# Displaying output value for combined GPA.
print("Combined GPA: %.1f" % final_GPA)
