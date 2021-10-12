## A progam that generates a ceaser cipher, a simple encoding technique that
# simply shifts each letter by a specified number of places along the alphabet.
# Does not affect non-letters and can program can also be used to decode
# (negative shift) ##

### I tried to figure this out but my code got way too complicated. Ben shows
# in his answer that a good way to tackle the 'wrapping around' in a list or
# string to find the new index after a shift is as follows: take the index of
# the old value, add the shift amount and then % by the length of the list/string.
# For example if the new shifted index is 3 in a length of 26, then the new
# index is simply 3. Or, if the old index is 25 and gets shifted up by 4,
# the shifted index is now 29; again 29 % 26 = 3 (same as counting, wrapping
# around: 25, 26, 1, 2, 3).
# If the new shifted index is a negative number it also works. If the original
# index is 2 and gets shifted by -4 to -2,
# -2 % 26 = 24
# This is the same as counting back: 2, 1, 26, 25, 24.
# The actual formula to work out the modulo divider operator '%' shows that this
# works. I cannot think about how this actually works without writing down the
# equation each time so just trust it, this is the cleanest way to deal with
# list/string wrap arounds. ###
