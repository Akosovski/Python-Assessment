def super_sums(x):
    # write your codes here
    total_sum = 0

    for i in range(1, x + 1):
        row_sum = sum(range(1, i + 1))
        total_sum += row_sum

    return total_sum


print(super_sums(3))