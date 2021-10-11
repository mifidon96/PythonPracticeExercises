# A program that reads a GPA score from the user and reports a letter grade.
# Must round to the nearest grade if score is inbetween grade thresholds. #

from statistics import mean

Ap = 4.0
A = 4.0
Am = 3.7
Bp = 3.3
B = 3.0
Bm = 2.7
Cp = 2.3
C = 2.0
Cm = 1.7
Dp = 1.3
D = 1.0
F = 0

grade = float(input("Please enter a GPA score: "))

if grade >= mean((Ap,A)):
    answer = "A+"
elif grade >= mean((A,Am)):
    answer = "A"
elif grade >= mean((Am,Bp)):
    answer = "A-"
elif grade >= mean((Bp,B)):
    answer = "B+"
elif grade >= mean((B,Bm)):
    answer = "B"
elif grade >= mean((Bm,Cp)):
    answer = "B-"
elif grade >= mean((Cp,C)):
    answer = "C+"
elif grade >= mean((C,Cm)):
    answer = "C"
elif grade >= mean((Cm,Dp)):
    answer = "C-"
elif grade >= mean((Dp,D)):
    answer = "D+"
elif grade >= mean((D,F)):
    answer = "D"
elif grade < mean((D,F)):
    answer = "F"

print("Your letter grade equivalent is:", answer)
