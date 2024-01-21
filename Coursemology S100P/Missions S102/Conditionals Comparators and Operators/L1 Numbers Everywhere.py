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
        return "nay"
    else:
        return "yay"