# we use for loop to print something repeatedly without having to manually coding it

for asterisk in range(2):
    # RANDOM NOTE: to make it print starting with 1 instead of 0, use print("*", asterisk + 1)
    print("*", asterisk + 1, (asterisk + 1) * ".")

# RANDOM NOTE: There's also another way to do that
for asterisk in range(1, 6):
    print("-", asterisk, (asterisk) * ".")


for asterisk in range(1, 9, 2):
    print("+", asterisk, (asterisk) * ".")
# (start, end, step)
# In the step, it prints the last number and not the number after the count

# EXAMPLE: range(1, 9, 3), it works this way. Count 1..2..3 (the third count is what will be printed)

# NESTED LOOP
for x in range(3):
    for y in range(2):
        print(f"\n({x},{y})")

# Iterable
for p in "\nBabu\n":
    print(p)

# This and what's above are the same
b = "Babu"
for letters in b:
    print(letters)
    # Take note, we always need a var name in the loop and we will use it as storage for the declared variable and printing purposes.


for asterisk in range(1, 10, 3):
    print("+", asterisk, (asterisk) * ".")
# OUTPUT: 1, 4, 7 --> not 1, 4, 7, 10. range() function does not include/print the stop value, only the values before it.
