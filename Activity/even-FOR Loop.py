# EXERCISE: PRINT 2,4,6,8 \n We have 4 even numbers

count = 0
for m in range(1, 10):
    if m % 2 == 0:
        print(m)
        count += 1

print("We have", count, "even numbers")
