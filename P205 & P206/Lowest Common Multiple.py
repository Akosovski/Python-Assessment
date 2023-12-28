def greatestCommonDivisor(a, b):
    while b:
        a, b = b, a % b
    return a

def lowestCommonMultiple(a, b):
    return a * b // greatestCommonDivisor(a, b)

a = int(input("a: "))
b = int(input("b: "))

print(lowestCommonMultiple(a, b))