def primeNumbers(x):
    result = []
    # write your codes here
    for i in range(2, x):
        for j in range(2, x):
            if i % j == 0:
                break
        if i == j:
            result.append(i)
    return result


print(primeNumbers(10))
print(primeNumbers(100))
print(primeNumbers(1000))