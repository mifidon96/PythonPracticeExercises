# A programme that converts human years to dog years, with a conversion of
# the first two years equaling 10.5 human, and the rest equaling 4 human

name = input("Please enter your name: ")
age_human = float(input("Please enter your age: "))

if 0 <= age_human <= 2:
    age_dog = age_human * 10.5
    print("Wow %s, you're %.1f in dog years!" % (name, age_dog))
elif age_human > 2:
    age_dog = 4*(age_human-2) + 21
    print("Wow %s, you're %.1f in dog years!" % (name, age_dog))
else:
    print("%s... you're not THAT young." % name)
