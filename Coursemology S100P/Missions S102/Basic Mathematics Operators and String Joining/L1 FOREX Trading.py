# Question 1: Foreign Exchange Calculator
def calcFX(fxr, amountSGD):
    # write your codes here
    foreign_currency_amount = amountSGD / fxr
    return foreign_currency_amount

# Question 2: Foreign Exchange Report
def fxReport(curCode, fxRate, sgdAmount):
    foreign_currency_amount = sgdAmount / fxRate
    foreign_currency_amount = round(foreign_currency_amount)
    return f"For {sgdAmount} SGD, you will receive {foreign_currency_amount} {curCode}."

fxReport("MYR", 0.35, 5000) # Print
fxReport("RMB", 0.2, 5000) # Print