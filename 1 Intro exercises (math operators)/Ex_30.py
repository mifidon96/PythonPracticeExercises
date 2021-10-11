# A Program that reads a pressure from the user in kilopascals and displays
# the pressure in pounds per square inch, mmHg and Atm. ###

press_kpa = float(input("Please enter pressure in kilopascals: "))

press_psi = press_kpa * 0.145038
press_mmHg = press_kpa * 7.50062
press_atm = press_kpa * 0.00986923

print("Pressure in psi: %.2f \nPressure in mmHg: %.2f \nPressure in atm: %.2f" % (press_psi, press_mmHg, press_atm))
