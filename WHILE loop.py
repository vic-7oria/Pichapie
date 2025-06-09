# While loop will continue running as long as a condition is always true or always met

name = input("What's your name? ")

# Here, we will use if else only

'''
if name == "":
    print("Enter your name")
else:
    print(f"What's up {name}")
'''

# with if statment, it runs once. But with While loop, the program will not terminate


while name == "":
    print("Enter your name")
    name = input("What's your name? ")
else:
    print(f"What's up {name}")


# We can use "else" in while and it will not affect its output
#  but you can also remove it, and adjust it to proper indention

# Like this...
'''
while name == "":
    print("Enter your name")
    name = input("What's your name? ")

print(f"What's up {name}")
'''
