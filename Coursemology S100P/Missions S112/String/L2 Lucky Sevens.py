def lucky_seven(n):
    result_numbers = [str(i) for i in range(1, n+1) if i % 7 == 0 or '7' in str(i)]
    return ', '.join(result_numbers)

print(lucky_seven(100))