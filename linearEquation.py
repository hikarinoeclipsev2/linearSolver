def linearEquation(a, b):
    if (a == 0):
        print("No Solution")
    elif (a == b == 0):
        print("Infinite Solution")
    else:
        x = -b/a
        print("Solution: ", x)


print("Welcome to Linear Equation Solver")
print("The linear equation is in this format: ax + b = 0")
a = float(input("a? "))
b = float(input("b? "))

linearEquation(a, b)
