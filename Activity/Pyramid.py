rows = int(input("Enter rows: "))

'''
for i in range(row):
    for j in range(column):
        if j <= row-i or j >= row+i:
            print(" ")
        else:
            print("*")

    print("\n")
'''

# First
for i in range(1, rows + 1):
    for j in range(1, rows * 2):
        if rows - i < j < rows + i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Mix of multi line comment and First
row = int(input("Enter rows again: "))

for i in range(1, row + 1):
    for j in range(1, row * 2):
        if j <= row-i or j >= row+i:
            print("*", end="")  # this part made it inverted
        else:
            print(" ", end="")
    print()


# Experimental
row3 = int(input("Enter rows for the third time: "))

for i in range(1, row3 + 1):
    for j in range(1, row3 * 2):
        if j <= row-i or j >= row+i:
            # the print part of this basically reminded us the importance of END keyword
            # also the code from c doesn't work in python
            print(" ")
        else:
            print("*")
