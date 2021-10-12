#  A funciton that return the precedence of an operator, a string containing
# the operator is the function's only parameter. The function returns 1 for +/-,
# 2 for * and /, and 3 for ^ (order, not XOR boolean operator). If the string
# does not contain a mathematical operator then the function will return -1.
# main() program will read operator from the user, and either display the
# precedence or display an error message (when function returns -1) #

def precedence(s):
    if s == "+" or s == "-":
        return 1
    elif s == "*" or s == "/":
        return 2
    elif s == "^":
        return 3
    else:
        return -1

def main():
    string = input("Please enter a math operator: ")
    prec = precedence(string)
    if prec == 1 or prec == 2 or prec == 3:
        print("Precedence is:", prec)
    elif prec == -1:
        print("This is not a math operator.")

if __name__ == "__main__":
    main()
