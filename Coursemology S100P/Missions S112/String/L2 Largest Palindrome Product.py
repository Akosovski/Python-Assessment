def is_palindrome(number):
    return str(number) == str(number)[::-1]

def palindrome(maxInt):
    largest_palindrome = 0

    for i in range(maxInt, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome

print(palindrome(999))