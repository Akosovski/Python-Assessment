def financialSavings(baseMoney, monthlyDeposit, interestAnnual, months):
    # write your codes here

    if interestAnnual != 0: 
        monthly_interest_rate = interestAnnual / 12 / 100

    for i in range(1, months+1):
        baseMoney += monthlyDeposit
        if interestAnnual != 0:
            interest = baseMoney * monthly_interest_rate
            baseMoney += interest
    
    # 1st month not covered
    baseMoney -= monthlyDeposit
    rounded = round(baseMoney)

    return rounded

print(financialSavings(500, 0, 0, 12))
print(financialSavings(500, 10, 0, 12))
print(financialSavings(500, 0, 12, 12))
print(financialSavings(500, 10, 12, 12))