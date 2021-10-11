# A program that reads a wavelength value from the user and reports its colour.
# An appropriate error message is displayed if the wavelength is outside the
# visible light spectrum #

wavelen = float(input("Please enter a wavlength within the visibile light spectrum (nm): "))
colour = ""

if 380 > wavelen > 750:
    print("This value is outside the visible light spectrum")

elif 380 <= wavelen < 450:
    colour = "Violet"
elif 450 <= wavelen < 495:
    colour = "Blue"
elif 495 <= wavelen < 570:
    colour = "Green"
elif 570 <= wavelen < 590:
    colour = "Yellow"
elif 590 <= wavelen < 620:
    colour = "Orange"
elif 620 <= wavelen <= 750:
    colour = "Red"

if colour != "":
    print("This wavelength corresponds to the colour, %s." % colour)
