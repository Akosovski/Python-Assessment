def dataType(list):
    # write your codes here
    result = ""
    for i in range(len(list)):
        container = str(list[i])
        result = result + container
    return result
    

print(dataType([4,6.78,'hello',45,'world']))