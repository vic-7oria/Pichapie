# {value:flags}
# we format a value based on the flags we put

grade1 = 94.4654328
grade2 = 95.288656
grade3 = 99.5423

money1 = 4543843.63465548
money2 = -78654466.4348883
money3 = 56654678.6682164


# These prints the first 3 decimals of the value
print(f"Your Grade1 is {grade1:.3f}")
print(f"Your Grade2 is {grade2:.3f}")
print(f"Your Grade3 is {grade3:.3f}\n")

# moved to fill until 10th
print(f"Your Grade1 is {grade1:10}")
print(f"Your Grade2 is {grade2:10}")
print(f"Your Grade3 is {grade3:10}\n")

# Right padded
print(f"Your Grade1 is {grade1:>20}")
print(f"Your Grade2 is {grade2:>20}")
print(f"Your Grade3 is {grade3:>20}\n")

# center padded
print(f"Your Grade1 is {grade1:^20}")
print(f"Your Grade2 is {grade2:^20}")
print(f"Your Grade3 is {grade3:^20}\n")

# it adds comma for hundreds, thousands
# the plus here indicates that the number is positive
print(f"Your Money1 is {money1:+,}")
print(f"Your Money2 is {money2:+,}")
print(f"Your Money3 is {money3:+,.4f}\n")
