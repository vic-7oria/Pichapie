# Simple Somparison
grade = 100
if grade > 30:
    print("ok")
elif grade != 50:
    print("chill")
else:
    print("woah")


# Comparison with limited range
# age = input("Input Age: ")
''''
if int(age) > 18:
    message = "Adult"
elif int(age) <= 18 and int(age) >= 13:
    message = "Teen"
elif int(age) < 12 and int(age) >= 1:
    message = "Kid"
else:
    message = "Infant"

print(message)
'''

# checking if age is between 18 and 50
age = input("Input Age: ")
# if int(age) >= 18 and int(age) < 50: #this is same with...

if 18 <= int(age) < 50:

    print("In!")
else:
    print("Out of range :<")
