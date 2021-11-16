## Recursive function that determines if a string is a palindrome. Empty strings,
# one letter strings and two same-letter strings are considered palindromes also.
# main() function will read a string from the user. Can be case sensitive. ##

def main():
    word = input("Please input a word: ")
    if isPalindrome(word):
        print(f"'{word}', is a palindrome")
    else:
        print(f"'{word}', is not a palindrome")

# Funciton that returns True if the word argument is a palindrome
def isPalindrome(word, f_i=0):
    # updating backward index to compare letter at forward index
    b_i = -(f_i+1)
    # Escape if middle letter of an odd numbered word/ the letter before the
    # middle gap of an even numbered word is reached, returning True
    if f_i == len(word)//2 and word[f_i] == word[b_i]:
        return True
    elif word[f_i] == word[b_i]:
        return True and isPalindrome(word, f_i+1)
    # Escape if letters do not match returning False
    else:
        return False

if __name__ == "__main__":
    main()
