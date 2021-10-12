## A main() program that uses functions from Ex_94 and Ex_96 that generates a
# random strong password and displays it while also displaying the number of
# attempts to generate it.

def main():
    from Ex_94 import randPass
    from Ex_96 import passIsStrong

    attempt = 0
    result = False

    while result is False:
        random_password  = randPass() # returns a string
        result = passIsStrong(random_password) # returns a boolean
        attempt += 1

    print(random_password, "was generated after attempt no.", attempt)

main()
