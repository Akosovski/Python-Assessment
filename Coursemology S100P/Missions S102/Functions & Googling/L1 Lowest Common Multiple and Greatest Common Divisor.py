# Question 1: Lowest Common Multiple

def greatestCommonDivisor(a, b):
    while b:
        a, b = b, a % b
    return a

def LCM(a, b):
    return a * b // greatestCommonDivisor(a, b)

# Question 2: Greatest Common Divisor
def GCD(a, b):
    while b:
        a, b = b, a % b
    return a
