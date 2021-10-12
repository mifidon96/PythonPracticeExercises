## A program that reads a mathematical expression in infix from the user,
# converts it to a postfix expression, then evaluates it and displays its value.
# The algorithm for the evaluation of a postfix expression is provided in the
# question. ###

# Importing modules
from Ex_122 import mathToken
from Ex_123 import infix2Postfix

def isNumber(n):
    # if variable == null or empty data type
    if not n:
        return False
    # Checking if n is a number
    answer = True
    n = str(n)
    for char in n:
        if char not in "1234567890.x":
            answer = False
    return answer

# Reading user input
expression = input("Please input a mathematical expression: ")
# Generating postfix expression
postfix = infix2Postfix(mathToken(expression))
# Initialising empty list for values
values = []
for token in postfix:
    if isNumber(token):
        values.append(int(token))
    else:
        # evaluation result of the last two operands with the operator (token)
        # inbetween
        right = str(values.pop())
        left = str(values.pop())
        if token == "^":
            token = "**"

        eval_str = left + token + right
        values.append(eval(eval_str))

print("The expression evaluates to:", values[0])
