def maxRoses(money, redCost, whiteCost):
    total_red = 0
    total_white = 0
    budget = 0

    if money <= 0:
            return "Invalid input. Money must be a positive number."

    while money > budget:
        if total_white <= (total_red / 2):
            total_red = total_red + 1
            budget += redCost
            total_white = total_white + 1
            budget += whiteCost
        else:
            total_red = total_red + 1
            budget += redCost

    while money < budget:
        total_red -= 1
        budget -= redCost
        
    total_red += 1
    total_white -= 1
    return f"{total_red},{total_white}"

print(maxRoses(60, 3.8, 2.7))
print(maxRoses(50, 2, 1.50))