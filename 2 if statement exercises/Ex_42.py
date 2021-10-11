# Programme that reads a frequency in Hz provided by the user and matches it
# +/- 1 Hz to a note in the fourth octave, otherwise reporting that the note
# does not exist

# Initialising lists of notes in the fourth octave and their corresponding exact
# frequencies. Also intitaizing match marker (x).
NOTES = ["C4", "D4", "E4", "F4", "G4", "A4", "B4"]
FREQ = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]
x = 0
# Prompting an input of a frequency value from the user
freq = float(input("Please enter a frequency value in Hz: "))
# Looping through the FREQ list
for e in FREQ:
    # Condidtion if freq is +/- 1 Hz of FREQ elemnt
    if e - 1 <= freq <= e + 1:
        # Note is pulled from NOTES list at same index as e in FREQ
        note = NOTES[FREQ.index(e)]
        # Display statement if user enters exact frequency of the note
        if freq == e:
            print("%.2f Hz corresponds exactly to %s." % (freq, note))
            # x = 1 is a marker for a frequency-to-note match
            x = 1
        # Display statement if user gets within +/- 1 Hz of exact frequency
        else:
            print("%.2f Hz corresponds roughly to %s." % (freq, note))
            # x = 1 is a marker for a frequency-to-note match
            x = 1
# If x != 1 (the match marker), then no match has been found and displays an
# "unsuccessful" message to the user
if x == 0:
    print("I'm sorry but that frequency does not correspond to a note.")
