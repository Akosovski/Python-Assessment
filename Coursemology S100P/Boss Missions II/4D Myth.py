import random

def generate_lucky_number():
    lucky_num = ""
    for i in range(4):
        lucky_num += str(random.randint(0, 9))
    return lucky_num

def set_bet_number():
    bet_num = ""
    for i in range(4):
        bet_num += str(random.randint(0, 9))
    return bet_num

def check_win(bet_number, lucky_number):
    jackpot = 3000
    if bet_number == lucky_number:
        return jackpot
    else:
        return 0

def first_bet_technique():
    total_bets = 0
    total_winnings = 0

    for x in range(10000):
        bet_number = ""
        for y in range(4):
            bet_number += str(random.randint(0, 9))
        lucky_number = generate_lucky_number()

        total_bets += 1
        total_winnings += check_win(bet_number, lucky_number)
    print(total_bets)
    return total_winnings / total_bets

def second_bet_technique():
    total_bets = 0
    total_winnings = 0

    for x in range(10000):
        bet_number = ""
        for y in range(4):
            bet_number += str(random.randint(0, 9))
        lucky_number = generate_lucky_number()

        avoid_numbers = set(lucky_number)
        while any(digit in avoid_numbers for digit in bet_number):
            bet_number = set_bet_number()

        total_bets += 1
        total_winnings += check_win(bet_number, lucky_number)

    print(total_bets)
    return total_winnings / total_bets

def lottery():
    first_bet_result = first_bet_technique()
    second_bet_result = second_bet_technique()

    return f"{first_bet_result:.2f} {second_bet_result:.2f}"

print(lottery())