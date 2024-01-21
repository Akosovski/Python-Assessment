def coinSums(x):
    coins = [1, 5, 10, 20, 50, 100]
    
    ways = [0] * (x + 1)
    ways[0] = 1
    
    for coin in coins:
        for amount in range(coin, x + 1):
            ways[amount] += ways[amount - coin]
    
    return ways[x]

result1 = coinSums(10)
print(result1) 

result2 = coinSums(50)
print(result2)
