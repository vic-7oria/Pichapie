# Activity
# no more than 12 characters
# no spaces
# no digits

user = input("Enter username: ")

if len(user) > 12:
    print("It must not exceed 12 Characters")
elif not user.find(" ") == -1:
    print("It cannot have spaces")
elif not user.isalpha():
    print("It cannot have digits")
else:
    print(f"Hello {user}")
