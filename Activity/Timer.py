import time
# We need to import a time module

# to make the timer sleep for 3 secs, use...

'''
time. sleep(3)

print("Time!")
'''

timer = int(input("Enter a timer in secs: "))

for z in range(0, timer):
    print(z)
    # this acts as a delay in each seconds in the input, it puts each second into sleep.
    time.sleep(2)

print("Time's up!")


# REVERSED countdown
for z in range(timer, 0, -1):
    print(z)
    # this acts as a delay in each seconds in the input, it puts each second into sleep.
    time.sleep(1)

print("Time's up!")


# DIGITAL CLOCK type shi
for z in range(timer, 0, -1):
    secs = z % 60  # 60 for idk really, Bro Code just put it w/o exp.
    print(f"00:00:{secs:02}")

    # to print 0 on the left of single digits. 0 is the padding and 2 means two digits as a format.

    # this acts as a delay in each seconds in the input, it puts each second into sleep.
    time.sleep(1)

print("Time's up!")
