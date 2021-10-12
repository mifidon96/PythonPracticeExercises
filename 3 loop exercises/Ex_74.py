## A program that generates and displays a multiplication table, 1 - 10, with
# labels. ###

# Top line; horizontal label generation
print("        ", end="")
for hl in range(1,11):
    if hl == 10:
        print("%4d    " % hl)
    else:
        print("%4d    " % hl, end="" )

# Rest of table including vertical label

for vl in range(1,11):
    print("%4d    " % vl, end="" )
    for e in range(1,11):
        n = vl * e
        if e == 10:
            print("%4d    " % n)
        else:
            print("%4d    " % n, end="" )
