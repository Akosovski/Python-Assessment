import random

def generate_lucky_number():
    return ''.join(str(random.randint(0, 9)) for _ in range(4))

def calculate_winnings(bet_number, lucky_number):
    return 3000 if bet_number == lucky_number else 0

def first_betting_technique():
    total_bets = 0
    total_winnings = 0

    for _ in range(10000):
        bet_number = ''.join(str(random.randint(0, 9)) for _ in range(4))
        lucky_number = generate_lucky_number()

        total_bets += 1
        total_winnings += calculate_winnings(bet_number, lucky_number)

    expected_return = total_winnings / total_bets
    return expected_return

def second_betting_technique():
    total_bets = 0
    total_winnings = 0

    for _ in range(10000):
        bet_number = ''.join(str(random.randint(0, 9)) for _ in range(4))
        lucky_number = generate_lucky_number()

        # Avoid numbers from the lucky number in the prior round
        avoid_numbers = set(lucky_number)
        while any(digit in avoid_numbers for digit in bet_number):
            bet_number = ''.join(str(random.randint(0, 9)) for _ in range(4))

        total_bets += 1
        total_winnings += calculate_winnings(bet_number, lucky_number)

    expected_return = total_winnings / total_bets
    return expected_return

def lottery():
    expected_return_first_technique = first_betting_technique()
    expected_return_second_technique = second_betting_technique()

    return f"{expected_return_first_technique:.2f} {expected_return_second_technique:.2f}"

# Example usage
result = lottery()
print(result)