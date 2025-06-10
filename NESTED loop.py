# In the nested loop, it can be a mix of for and while loop

for x in range(3):  # in the OUTER LOOP range is basically the number of repetition of what we will print in the INNER LOOP
    for y in range(1, 11):
        # the END keyword is used to set the format of the output, bcs usually it prints [end="\n"] (as default)
        print(y, end="")
        # this empty string means no spaces between the numbers and it will print horizontally

    print()  # this is used to print each iteration on a new line
