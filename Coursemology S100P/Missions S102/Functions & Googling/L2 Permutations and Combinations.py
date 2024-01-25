import math

# Question 1: Generate the factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
# Question 2: Generating permutations of r items from n items (Use the factorial)
    
def permute(n,r):
    # write your codes here
    n_factorial = factorial(n)
    divisor_factorial = factorial(n-r)

    result = n_factorial / divisor_factorial
    return result

# Question 3: Generating combinations of r items from n items (Use the factorial)

def combine(n,r):
    # write your codes here
    n_factorial = factorial(n)
    first_divisor_factorial = factorial(n-r)
    second_divisor_factorial = factorial(r)

    divisor = first_divisor_factorial * second_divisor_factorial
    result = n_factorial / divisor

    return round(result)

# print(permute(10,4))
print(combine(10,4))