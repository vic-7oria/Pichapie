unit = input("Dollar or Peso? (D or P): ").upper() or input("Dollar or Peso? (D or P): ").lower()
amount = float(input("Enter amount: "))

if unit == "D":
    print(amount * 55.78, "dollar")
elif unit == "P":
    print(amount / 55.78, "peso")
else:
    print("Invalid Unit")

# EZ PZ
