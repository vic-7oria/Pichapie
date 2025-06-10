# SET =  {} unordered and immutable, Does not print dupe
# LIST = [] similar to array, ordered and changebale. Prints dupe
# TUPLE = () ordered and unchangeable. Prints dupe

# LIST
name = ["Gab", "Kiz", "Irish", "V", "Kheymp"]
print(name)


name[0] = "Queency"

# Method
name.append("PJ")
name.reverse()
name.sort()
name.insert(0, "hey")
# name.remove("hey")

print(name.index("Queency"))
print("Ryan" in name)

for x in name:
    print(x)


# SET
names = {"Gab", "Kiz", "Irish", "V", "Kheymp"}

names.pop()  # it will remove a random element
names.add("Lheane")


print(names)


for y in names:
    print(y)

# TUPLE
# for tuple, it works the same, but I think it only has limited methods.

namess = ("Gab", "Kiz", "Irish", "V", "Kheymp")

print(namess)
print("Queency" in namess)
print(len(namess))


for z in names:
    print(z)


# Print(dir(name)) dir function displays attributes and methods u can do
#  Print(help(name)) help function displays description of the attributes and methods
