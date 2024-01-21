def powerUp(x):
    string_x = str(x)
    power = string_x[-1]
    sliced_x = string_x[:-1]
    
    power = int(power)
    sliced_x = int(sliced_x)
    result = sliced_x ** power
    return result

powerUp(123) # Print
powerUp(12) # Print
