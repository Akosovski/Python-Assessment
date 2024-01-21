def powerUp(x):
    last_digit = x % 10
    all_except_last = x // 10

    return all_except_last ** last_digit