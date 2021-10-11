# A program that reads a number of decibels provided by user and makes a
# comparisen to real life

# Setting up two lists with sounds and their corresponding decibel readings
sounds = ["a quiet room", "an alarm clock", "a gas lawnmower", "a jackhammer"]
decibels = [40, 70, 106, 130]

# Taking decibel input from user
decibel = float(input("Please enter a number of decibels: "))

# Displaying messeges to the user if they enter decibel readings outside the
# decibel range in the decibels list.
if decibels[0] > decibel:
    print("That is really quiet. Even quieter than %s." % sounds[0])
elif decibels[len(decibels)-1] < decibel:
    print("That is really loud! Even louder than %s." % sounds[len(sounds)-1])

# If decibel input meatches exactly to an element in the decibels limit, it will
# display this to the user.
if decibel in decibels:
    sound = sounds[decibels.index(decibel)]
    print("That is as loud as %s." % sound)

# If the decibel reading is inbetween the values of two elemnts in the decibels
# list, the program will display what values this lies between
for i in range(0,len(decibels)-1):
    if decibels[i] < decibel < decibels[i+1]:
        print("That level of noise is somewhere between %s and %s." % (sounds[i], sounds[i+1]))
