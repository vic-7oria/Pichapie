# SET =  {} unordered and immutable
# LIST = [] similar to array, ordered and changebale
# TUPLE = () ordered and unchangeable

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

names.add("Lheane")

print(names)
