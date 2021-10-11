# This program returns the frequency of a note entered by the user. the notes
# are inputtd in the form e.g. "C4", where the letter is the note and the number
# is the octave

# Generating start list of octave 4 notes and thier corresponding frequencies
NOTES = ["C4", "D4", "E4", "F4", "G4", "A4", "B4"]
FREQ = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]

# Prompting input from user to enter note and octave
note = input("Please input the note and octave (e.g. C4) you would like to know the frequency for in Hz: ")

# Separating the letter and octave of the inputted note
letter = note[0]
octave = note[1]

# Case for exact match in note and NOTES list element
if note in NOTES:
    print("%s is %.2f Hz" % (note, FREQ[NOTES.index(note)]))
# If not exact match, looping through the NOTES list, looking for when the firt
# character of an element matches the letter (first character) of the inputted note.
elif note not in NOTES:
    for element in NOTES:
        if element[0] == letter:
            # Aquiring the corresponding frequency (basefreq) from FREQ list, as a
            # value to calculate the new frequency with
            basefreq = FREQ[NOTES.index(element)]
            # Using formula to calculate the new frequency (newfreq) freq/ 2**4-x
            # where x is the octave number
            newfreq = basefreq / 2**(4-float(octave))
            # Displaying the inputted note and the calculated new frequency
            print("%s is %.2f Hz" % (note, newfreq))
