def noDuplicates(list):
    tobeDeleted = []
    # write your codes here
    for i in range(len(list)):
        for j in range(len(list)):
            if i == len(list):
                break
            elif list[i] == list[j] and list[j] not in tobeDeleted:
                tobeDeleted.append(list[j])
    return tobeDeleted


print(noDuplicates([8, 30, 45, 8, 88, 120, 155, 76, 155]))