def coin_sum(value, ten_cent, fifty_cent):
    #write your codes here
    ten_cent_value = 10
    fifty_cent_value = 50

    total_ten = ten_cent_value * ten_cent
    total_fifty = fifty_cent_value * fifty_cent

    total = total_ten * total_fifty

    if value <= total:
        return True
    elif value > total:
        return False
    else:
        return False
    
print(coin_sum(150,6,2))