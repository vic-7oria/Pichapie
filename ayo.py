# print(1 * 8)


y = 35
x = 6
result = x*y
# print(result)


# ACCESSING CONTENTS OF A VARIABLE

Name = "Queency Ruth"
# print(Name)

# print("Total length: ",  len(Name))

# print("Access the letter: ",  Name[8])

# print(Name[0:3])

name = "Quee\n\"ncy \'Ruth"
# print("This is an experimental:", name)


# FORMATTED STRINGS

first_Name = "Queency"
last_Name = "Reyes"

# Full = first_Name + " " + last_Name
# Output: Queency Reyes

# but we can also do this, it has same output
Full = f"{first_Name} {last_Name}"
# print(Full)


# STRING MANIPULATION

myName = "Queency \"GorGeous\" Reyes"

'''
print(myName.upper())
print(myName.lower())
print(myName.title())
print(myName.find("GorG"))  # returns the index

print("GorG" in myName)  # returns boolean
'''

# TYPE CONVERSION
# t = input("x: ")

# we converted the string in the input so that the types are compatible
# y = int(t) + 1

# print(f"x: {t} y:{y}")


# CONDITIONAL STATEMENTS

'''
grade = 100
if grade > 30:
    print("ok")
elif grade != 50:
    print("chill")
else:
    print("woah")
'''


age = input("Input Age: ")


if int(age) > 18:
    message = "Adult"
elif int(age) <= 18 and int(age) >= 13:
    message = "Teen"
elif int(age) < 12 and int(age) >= 1:
    message = "Kid"
else:
    message = "Infant"

print(message)



#Age Classification but with while loop
age = input("Input Age: ")


while age != "stop":    
    if int(age) > 18 and int(age)<120:
        message = "Adult"
    elif int(age) <= 18 and int(age) >= 13:
        message = "Teen"
    elif int(age) < 12 and int(age) >= 1:
        message = "Kid"
    elif int(age) == 0:
        message = "Newborn"
    else:
        message = "Invalid Input"
       
    print(message)
    age = input("Input Age: ")
