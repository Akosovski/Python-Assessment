def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def biggestPrime(n):
    # Check numbers starting from n and going downwards
    for i in range(n, 1, -1):
        if is_prime(i):
            return i
        
print(biggestPrime(1000))
print(biggestPrime(100))
