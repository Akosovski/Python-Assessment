
def monotonic_checker(numbers):
    increasing = True
    decreasing = True

    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            increasing = False
        if numbers[i] < numbers[i + 1]:
            decreasing = False

    return increasing or decreasing

print(monotonic_checker([2, 4, 6, 8]))
print(monotonic_checker([2, 4, 1, 8]))