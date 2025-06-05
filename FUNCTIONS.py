# myName is the Parameter
def greet(myName):
    print(f"Happy\n Birthday! \n {myName}")


# "Queency" is the Argument
greet("Queency")


# NOTE: Parameter is the input that you define (or declare ? ) for ur function, while Argument is the actual value of the Parameter

# FUNCTION THAT DOES A TASK
def getGreet(name):
    return f"Nice to meet you, {name}!"


message = getGreet("Kwens")
print(message)


# FUNCTION THAT CALCULATES
def calc(number, by):
    return number + by

# to print the output of the function above, we need to store the arguments in a variable, and we can print that variable.


result = calc(3, 5)
print(result)
