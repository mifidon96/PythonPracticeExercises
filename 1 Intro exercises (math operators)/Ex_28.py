# Programme that determines wind chill index (rounded to the closest integer),
# taking air temperature and wind speed from the user

Ta = float(input("Please input air temperature: "))
V = float(input("Please input wind speed: "))

WCI = 13.12 + 0.6215*Ta - 11.37*V**0.16 + 0.3965*Ta*V**0.16

print("WCI is", round(WCI))
