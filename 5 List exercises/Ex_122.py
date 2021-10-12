## Tokenizing is the process of converting a string into a list of substrings,
# known as tokens. A list of tokens is often easier to work with than a string
# as a string may have irregular spacing. In some cases, substantial work is
# needed to determine where one token ends and the next one begins. In maths,
# tokens are items such as operators, numbers, and bracketts. *,/,! and () are
# easy to identify but + or - less so as they may be part of a number.
#
# This function will tokenize mathematical expressions. Each token should be a
# parenthesis, an operator, or a  number with an optinal leading +/-.
# Parameters: string containing a methematical expressino. Returns: the list of
# tokens.
# May assume string passed is always a valid mathematical expression with
# integers only. Function must be able to handle variable amounts of whitespace.
# main() program demonstrates function and is suitable for importing. ##


def mathToken(s):
    # Initialising constants and sting index "i"
    digits = "1234567890"
    token_list = []
    prev_char = ""
    i = 0

    # Removing all whitespace from string
    s = s.split()
    s = "".join(s)

    while i < len(s):
        # If the current character is an a operator excluding "+"/"-"
        if s[i] in ["*","/","^","(",")"]:
            token_list.append(s[i])
            prev_char = s[i]
            i += 1
        # The current character is a "+"/"-" operator
        elif (s[i] == "+" or s[i] == "-") and (prev_char in digits or prev_char == ")"):
            token_list.append(s[i])
            prev_char = s[i]
            i += 1
        # The current character is part of a number including "+"/"-"
        else:
            # Include the "+"/"-" in token list entry then add to entry until
            # an operator is detected
            item = s[i]
            prev_char = s[i]
            i += 1
            while i < len(s) and s[i] not in ["*","/","^","(",")","+","-"]:
                item += s[i]
                prev_char = s[i]
                i += 1
            token_list.append(item)

    return token_list

def main():
    s = input("Please enter a mathematical expression to return a list of tokens: ")
    print(mathToken(s))

if __name__ == "__main__":
    main()
