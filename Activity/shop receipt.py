# Initialize your varibales where you will store the lists in the Shop Cart
foods = []  # means we will use list, for organized elements
prices = []
total = 0

# We will use While loop to make the user input their order
while True:
    askFood = input("Enter food you want (Press p to print reciept): ")

    if askFood.lower() == "p":  # we need the .lower() function so that it will convert the upcase P to match the right side of comparison
        break
    elif askFood == "":
        print("Please enter the item")
    else:
        putPrice = int(input(f"Enter the price of {askFood}: "))
        foods.append(askFood)
        prices.append(putPrice)

print("\n******* RECEIPT *******\n")

print(f"The items are:")

for f, p in zip(foods, prices):
    # {f:<10}{p:>5} is the reason why the prices are aligned
    print(f" {f:<10}{p:>5} php")

print()  # this prints an line empty line


# simple calculation for the total price
for p in prices:
    total += p
print(f"Your total is {total} Pesos")
