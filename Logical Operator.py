# AND

Yo = True
Ya = True

Ye = False

if Ya and Yo:
    print("Both Are True!\n")
else:
    print("One of them are false\n")


# OR
if Ya or Yo:
    print("Either one or both of them are True!\n")
else:
    print("Both of them are false\n")


# TERNARY
if (Ya or Yo) and not Ye:
    print("All of them are True!\n")
else:
    print("Both of them are false\n")
