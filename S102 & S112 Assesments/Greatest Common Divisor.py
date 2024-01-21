def greatestCommonDivisor(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("a: "))
b = int(input("b: "))

print(greatestCommonDivisor(a, b))