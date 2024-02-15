import random

def QNS1():

    dollars = 1

    even_numbers = []
    for x in range(0, 37, 2):
        even_numbers.append(x)
    
    odd_numbers = []
    for y in range(1, 37, 2):
        odd_numbers.append(y)

    # Expected Earning = (Probability of Winning × Amount Won) − (Probability of Losing × Amount Lost)

    expected_earnings = ((len(odd_numbers) * dollars) - len(even_numbers) * dollars) / 37
    return round(expected_earnings, 3)

def QNS2(simulation_count):
    total_wins = 0
    total_losses = 0
    total_rounds = 0

    for x in range(simulation_count):
        wealth = 1
        spin_result = None
        rounds = 0

        while spin_result != 0:
            bet_amount = wealth
            spin_result = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36])
            
            if spin_result % 2 == 0: 
                total_wins += 1
                wealth += bet_amount
                break
            else:
                total_losses += 1
                wealth *= 2

            rounds += 1

        total_rounds += rounds

    average_rounds = total_rounds / simulation_count

    return round(average_rounds)

def roulette():
    return f"{QNS1()}0 {QNS2(10000)}"

print(roulette())