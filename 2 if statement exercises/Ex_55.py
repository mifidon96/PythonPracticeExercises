# A program that reads a frequency value (Hz) for an electromagnetic wave and
# displays its named designation e.g. radio waves, microwaves, X-rays etc. #

freq = float(input("Please enter electromagnetic wave frequency (Hz) in the form, xey = x*(10**y): "))

if freq < 3e9:
    wave_type = "Radio wave"
elif 3e9 <= freq < 3e12:
    wave_type = "Microwave"
elif 3e12 <= freq < 4.3e14:
    wave_type = "Infrared"
elif 4.3e14 <= freq < 7.5e14:
    wave_type = "Visible light"
elif 7.5e14 <= freq < 3e17:
    wave_type = "UV"
elif 3e17 <= freq <= 3e19:
    wave_type = "X-ray"
elif 3e19 <= freq:
    wave_type = "Gamma ray"

print("A wave at this frequency falls within the %s range." % wave_type)
