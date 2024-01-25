def coinSums(x):
    # Define the available coin denominations
    coins = [1, 5, 10, 20, 50, 100]

    # Initialize an array to store the number of ways for each amount from 0 to x
    ways = [0] * (x + 1)

    # There is one way to make change for 0 cents (no coins)
    ways[0] = 1

    # Iterate through each coin denomination
    for coin in coins:
        # Update the ways array for each amount from coin to x
        for amount in range(coin, x + 1):
            ways[amount] += ways[amount - coin]

    return ways[x]

print(coinSums(10))
print(coinSums(50))