unit = input("Dollar or Peso? (D or P): ").upper() or input("Dollar or Peso? (D or P): ").lower()
amount = float(input("Enter amount: "))

if unit == "D":
    print( f"The amount converted from {amount} Peso is {amount * 55.78} dollar/s")
elif unit == "P":
    print(f"The amount converted from {amount} Dollar is {amount / 55.78} peso")
else:
    print("Invalid Unit")

# EZ PZ
