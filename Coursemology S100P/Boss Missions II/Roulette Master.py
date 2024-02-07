import random

def earning_per_bet():
    total_bets = 0
    total_win = 0

    for x in range(10000):
        result = random.randint(0, 36)
        bet_amount = 1

        if result == 0:
            total_win -= bet_amount
        elif result % 2 == 0:
            total_win += bet_amount

        total_bets += bet_amount

    return total_win / total_bets

def earning_per_round():
    total_rounds = 0
    total_wealth = 0

    for y in range(100000):
        wealth = 0
        bet_amount = 1
        rounds = 0

        while True:
            result = random.randint(0, 36)

            if result == 0:
                wealth -= bet_amount
                break
            elif result % 2 == 0:
                wealth += bet_amount
                break
            else:
                wealth -= bet_amount
                bet_amount *= 2
                rounds += 1

        total_wealth += wealth
        total_rounds += rounds

    return total_wealth / total_rounds

def roulette():
    return f"{earning_per_bet():.2f} {earning_per_round():.2f}"

print(roulette())