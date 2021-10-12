## Function that determines wether a triangle can be made from three side lengths
# as its parameters; supplies by the user. Returns a boolean result. Main()
# function to demonstrait its use ##

def triangle(a,b,c):
    a,b,c = float(a), float(b), float(c)
    if a >= b + c:
        return False
    elif b >= a + c:
        return False
    elif c >= a + b:
        return False
    else:
        return True

def main():
    a = input("Please enter a side length: ")
    b = input("Please enter a side length: ")
    c = input("Please enter a side length: ")
    if triangle(a,b,c):
        print("These sides can make a triangle.")
    else:
        print("These sides cannot make a triangle.")

main()
