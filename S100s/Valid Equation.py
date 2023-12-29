def isEquationValid(x, y, z):
    result = 0
    if x + y == z:
        result += 1
    if x - y == z:
        result += 1
    if x * y == z:
        result += 1
    if x / y == z:
        result += 1
    if result == 0:
        return 0
    else:
        return 1

x, y, z = input("").split()

x = int(x)
y = int(y)
z = int(z)

print(isEquationValid(x, y, z))