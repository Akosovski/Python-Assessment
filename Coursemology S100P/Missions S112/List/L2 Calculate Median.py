def median(listLength, list):
    result = 0
    list.sort()
    # write your codes here
    if listLength % 2 == 0:
        num1 = (listLength // 2) - 1
        num2 = listLength // 2
        result = (list[num1] + list[num2]) // 2
    else:
        num = listLength // 2
        result = list[num]
    return result

print(median(6,[1,3,8,18,25,30]))
print(median(5,[1,3,7,18,25]))