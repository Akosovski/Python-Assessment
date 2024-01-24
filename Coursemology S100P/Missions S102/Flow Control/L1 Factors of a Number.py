def compute_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return str(factors)[1:-1]

X = 16
print(compute_factors(X))