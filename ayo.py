# print(1 * 8)


y = 35
x = 6
result = x*y
# print(result)


# accessing contents of variable

Name = "Queency Ruth"
# print(Name)

# print("Total length: ",  len(Name))

# print("Access the letter: ",  Name[8])

# print(Name[0:3])

name = "Quee\n\"ncy \'Ruth"
# print("This is an experimental:", name)


# Formatted strings

first_Name = "Queency"
last_Name = "Reyes"

# Full = first_Name + " " + last_Name
# Output: Queency Reyes

# but we can also do this, it has same output
Full = f"{first_Name} {last_Name}"

# print(Full)


# String manipulation

myName = "Queency \"GorGeous\" Reyes"

'''
print(myName.upper())
print(myName.lower())
print(myName.title())
print(myName.find("GorG"))  # returns the index

print("GorG" in myName)  # returns boolean
'''

# type conversion
t = input("x: ")

# we converted the string in the input so that the types are compatible
y = int(t) + 1

print(f"x: {t} y:{y}")
