# we access elements using []
# [start : end : step]


sample = "0123-567-9-10-11-12-48-55215"

print(sample[0:25:2])

print(sample[::4])

# it will put the deafult, which is 0
print(sample[:2])

# it started to print from index 20 to the end
print(sample[20:])

# it printed the last digit
print(sample[-1])

# this basically counted from right to left, but the counting started with -1 instead of just 0
# well maybe because 0 belongs to the first element from the left
# yes, it makes sense
print(sample[-8])
