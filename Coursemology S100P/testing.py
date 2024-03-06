def monotonic_checker(numbers):
    increasing = all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
    decreasing = all(numbers[i] >= numbers[i + 1] for i in range(len(numbers) - 1))

    return increasing or decreasing

print(monotonic_checker([2,4,6,8]))
print(monotonic_checker([2,4,1,8]))