## A function that will convert imperial unit measurements (for cooking)
# into more appropriate higher units when upscaling a recipe.
# e.g. recipe calls for 4 tbsp, quadrupling recipe gives 16 tblsp == 1 cup
# Parameters: number of units (int), unit measure (str).
# Return: Measure using largest possible units (str)
# main() program to read and display input and output resp. ##

def redMeasure(unit_no, unit_measure):
    # unit_no parameter is a str. Initializing result.
    unit_no = int(unit_no)
    result = ""

    # first convert to teaspoons
    if unit_measure == "cp":
        unit_no = unit_no * (3*16)
    elif unit_measure == "tbsp":
        unit_no = unit_no * 3
    elif unit_measure == "tsp":
        unit_no = unit_no
    else:
        unit_error = True
        return False

    # Run down of converting from largest to smallest measures. If a non-zero
    # value for the number of that measure, then adding to result string.
    cups = unit_no // (3*16)
    if cups != 0:
        unit_no = unit_no % (3*16)
        result += str(cups) + " cp, "

    tbsp = unit_no // 3
    if tbsp != 0:
        unit_no = unit_no % 3
        result += str(tbsp) + " tbsp, "

    tsp = unit_no
    if tsp != 0:
        result += str(tsp) + " tsp, "

    # Formatting result string so last "," is replaced by a "."
    index_last_c = result.rfind(",")
    result = result[:index_last_c] + "."

    return result


def main():
    unit_measure = input("Please enter your unit measure (cp, tbsp or tsp): ")
    unit_no = input("Please enter the number of units: ")
    print(redMeasure(unit_no, unit_measure))

if __name__ == "__main__":
    main()
