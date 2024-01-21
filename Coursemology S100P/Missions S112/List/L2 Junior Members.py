def junior_numbers(numbers):
    result = []
    # write your codes here
    for i in range(len(numbers)):
        if i != 0 and i != len(numbers):
            if numbers[i-1] > numbers[i] and numbers[i+1] > numbers[i]:
                result.append(numbers[i])
    return result


print(junior_numbers([1,2,3,4,5,6,7,8]))
print(junior_numbers([2,1,3,4,3,5,7,6,8]))