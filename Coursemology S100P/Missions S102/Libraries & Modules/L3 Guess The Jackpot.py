import random

def play_guessing_game():
    jackpot = random.randint(1, 10)
    chances = 5

    while chances > 0:
        user_guess = random.randint(1, 10)

        if user_guess < jackpot:
            user_guess = random.randint(user_guess + 1, 10)
        elif user_guess > jackpot:
            user_guess = random.randint(1, user_guess)

        if user_guess == jackpot:
            print("You win!")
            return

        chances -= 1

    print("You lose.")

play_guessing_game()