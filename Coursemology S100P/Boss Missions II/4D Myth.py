
def first_bet_technique():
    probability_of_winning = 1 / 10000
    probability_of_losing = 1 - probability_of_winning
    
    amount_won = 3000
    amount_lost = 1
    
    expected_earning = (probability_of_winning * amount_won) - (probability_of_losing * amount_lost)
    
    return round(expected_earning, 4)

def second_bet_technique():

    probability_of_winning = 1 / 5040
    probability_of_losing = 1 - probability_of_winning

    amount_won = 3000
    amount_lost = 1
    
    expected_earning = (probability_of_winning * amount_won) - (probability_of_losing * amount_lost)
    
    return round(expected_earning, 4)

def lottery():
    first_bet_result = first_bet_technique()
    second_bet_result = second_bet_technique()

    return f"{first_bet_result} {first_bet_result}"

print(lottery())