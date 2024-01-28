def sumOfDigits(x):
    sum = 0
    x = str(x)
    x_list = []
    for i in range(len(x)):
        x_list.append(int(x[i]))
    for j in range(len(x_list)):
        sum += x_list[j]
    return sum

print(sumOfDigits(101))