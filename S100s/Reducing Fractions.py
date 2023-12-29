def greatestCommonDivisor(a, b):
    while b:
        a, b = b, a % b
    return a

def reduce(n, d):
    gcd = greatestCommonDivisor(n, d)
    
    numerator = n // gcd
    denominator = d // gcd
    
    return str(numerator) + "," + str(denominator)

print(reduce(8, 4))
print(reduce(9, 27))