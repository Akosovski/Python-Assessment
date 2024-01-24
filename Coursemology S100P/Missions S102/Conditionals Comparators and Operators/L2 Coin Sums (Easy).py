def coin_sum(value, ten_cent, fifty_cent):
    total_value = (ten_cent * 10) + (fifty_cent * 50)
    print(total_value)
    if total_value == value or (total_value > value and (total_value - value) % 10 == 0 and ten_cent >= (total_value - value) // 10):
        return True
    else:
        return False
    

print(coin_sum(20,0,4))
print(coin_sum(150,6,2))