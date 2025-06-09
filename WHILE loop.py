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


# ANOTHER EXAMPLE

artist = input(f"Who is your fav artist? \n (Press x to exit)\n")

while not artist == "x":
    print(f"I like {artist} too!")
    artist = input(f"Who is your another fav artist? \n (Press x to exit)\n")

print("Thanks for sharing!")


number = 100
while number > 0:
    print(number)
    number = number // 2
    # COMPOUND STATEMENT: number //= 2
    # this is an expression to print limited numbers, loop won't stop if don't have it.


inp = ""
while inp.lower() != "quit":
    inp = input("Enter here: ")
    print("Paste:", inp)

# SITUATION: what if the user enters an uppercase?
# ANSWER: Put [while inp.lower() != "quit":] this function to convert erthing to lower to match the lowercased "quit"


# SAME WITH WHAT'S ABOVE
command = ""
while True:
    command = input("Hephep: ")
    print("Hooray", command)

    if command == "stop":
        break
