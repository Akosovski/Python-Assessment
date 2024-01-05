def interestRate(r1, r2, n):
    spA = r1
    spB = r2
    interest = n
    accumulatedA = 0
    accumulatedB = 0

    money = 3000
    years = 5

    for x in range(1, years+1):
        rate = (spA / money) * 100
        peryear = rate * interest
        money += peryear
        accumulatedA += peryear

    for y in range(1, years+1):
        rate = (spB / money) * 100
        peryear = rate * 5
        money += peryear
        accumulatedB += peryear
    
    if accumulatedA > accumulatedB:
        return "Savings Plan A"
    elif accumulatedA < accumulatedB:
        return "Savings Plan B"
   
print(interestRate(5, 6, 4))
print(interestRate(9, 10, 6))