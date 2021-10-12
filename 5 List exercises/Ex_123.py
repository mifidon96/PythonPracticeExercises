## A function that converts from infix to postfix of a mathematical expression
# e.g. from '3 + 4' to '3 4 +', taking a list of tokens as the argument and
# returning a list of tokens in postfix form. Including a main program that
# demonstrates the function by reading an expression from the user in infix form
# and displaying it in postfix form. Algorithm for this function is provided
# in the question. ##

from Ex_122 import mathToken

def infix2Postfix(infix_list):
    operators = []
    postfix = []

    # assigning precedence to operators (except parentheses) in a lsit
    # of tuples = ((p,o1),(p,o2),...) WORKS
    prec = []
    for token in infix_list:
        if token == "^":
            prec.append(3)
        elif token == "/" or token == "*" :
            prec.append(2)
        elif token == "+" or token == "-":
            prec.append(1)
        else:
            prec.append(0)
    work_list = list(zip(prec, infix_list))

    digits = "1234567890x"
    for item in work_list:
        p = item[0]
        token = item[1]
        # Checking to see if token (string) is a number
        number = False
        for digit in digits:
            if digit in token:
                number = True
                postfix.append(token)
                break
        # If not number then token is an operator
        if not number:
            # If "(" then adding token and precedence to operators list
            if token == "(":
                operators.append(item)
            # If ")" then popping operators and adding to postfix until operator == "("
            elif token == ")":
                while operators and operators[-1][1] != "(":
                    postfix.append(operators.pop()[1])
                operators.pop()

            # If not a parenthesis and operator at top of stack is of a greater
            # precedence than the current token and the operators list is not empty#
            # then popping the tokens from operators onto the postfix.
            # Then adding the working token and precedence to stop of operators stack
            else:
                while operators and operators[-1][0] != "(" and p <= operators[-1][0] :
                    postfix.append(operators.pop()[1])
                operators.append(item)

    # pop remaining operators onto the postfix until operators stack is empty
    while operators:
        postfix.append(operators.pop()[1])
    return postfix


def main():
    s = input("Enter a mathematical expression: ")
    result_list = infix2Postfix(mathToken(s))

    result = " ".join(result_list)
    print(f"\nPostfix form: \n{result}")

if __name__ == "__main__":
    main()
