def coinSums(x):
    amount = 0
    for one in range(0, x//100 + 1):
        for fifty in range(0, x//50 + 1):
            for twenty in range(0, x//20 + 1):
                for ten in range(0, x//10 + 1):
                    for five in range(0, x//5 + 1):
                        for single in range(0, x//1 + 1):
                            if (one * 100 + fifty * 50 + twenty * 20 + ten * 10 + five * 5 + single * 1) == x:
                                amount = amount + 1
    return(amount)

print(coinSums(12))
print(coinSums(50))