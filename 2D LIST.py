# SET =  {} unordered and immutable, Does not print dupe
# LIST = [] similar to array, ordered and changebale. Prints dupe
# TUPLE = () ordered and unchangeable. Prints dupe. Faster than LIST


cars = ["Mustang", "R8", "Camaro", "i8", "GR86"]
brands = ["Ford", "Audi", "Chevrolet", "BMW", "Toyota"]
luxury = ["Rolls Royce", "Bentley", "Aston Martin", "Mercedes Benz", "Porsche"]

money = [cars, brands, luxury]

print(money[2][1])  # [row] Horizontal [column] Vertical


# This is same with line 1,2,3
# Just don't forget the commas in between lists
moneyy = [["Mustang", "R8", "Camaro", "i8", "GR86"],
          ["Ford", "Audi", "Chevrolet", "BMW", "Toyota"],
          ["Rolls Royce", "Bentley", "Aston Martin", "Mercedes Benz", "Porsche"]]

print(moneyy[1][0])
print()  # For separation of output purposes

for cars in moneyy:
    print(cars)
print()  # For separation of output purposes

for car in money:
    for All_items in car:
        print(All_items, end=" ")
    print()
print()  # For separation of output purposes

for car in money:
    for All_items in car:
        print(All_items)
    print()
