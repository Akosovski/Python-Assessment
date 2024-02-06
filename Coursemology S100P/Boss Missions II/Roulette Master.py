import random

def roulette():
    # Question 1: Expected earning for each bet
    total_bets = 0
    total_winnings = 0

    for _ in range(10000):
        result = random.randint(0, 36)
        bet_amount = 1

        if result == 0:
            total_winnings -= bet_amount
        elif result % 2 == 0:
            total_winnings += bet_amount

        total_bets += bet_amount

    expected_earning_bet = total_winnings / total_bets

    # Question 2: Expected earning for each round of Donald's strategy
    total_rounds = 0
    total_wealth = 0

    for _ in range(100000):
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

    expected_earning_strategy = total_wealth / total_rounds

    return f'{expected_earning_bet:.2f} {expected_earning_strategy:.2f}'

# Example usage
result = roulette()
print(result)