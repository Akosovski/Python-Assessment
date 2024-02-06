import random

def generateNumber():
    number = list(range(10))
    random.shuffle(number)
    return ''.join(map(str, number[:4]))

def countCowsBulls(secret, guess):
    cows = sum(s == g for s, g in zip(secret, guess))
    bulls = sum(s in secret for s in guess) - cows
    return cows, bulls

def main():
    print("Welcome to the cows and bulls game!")

    secret_number = generateNumber()
    attempts = 0

    while True:
        user_guess = input("Give me your best guess: ")

        if not user_guess.isdigit() or len(user_guess) != 4 or len(set(user_guess)) != 4:
            print("Invalid input. Please enter a 4-digit number with distinct digits.")
            continue

        attempts += 1
        cows, bulls = countCowsBulls(secret_number, user_guess)

        if cows == 4:
            print(f"\nThe secret number is {secret_number}. You won and took {attempts} tries.\n")
            break
        else:
            print(f"You have {cows} cow(s) and {bulls} bull(s)")
            print("Your guess isn't quite right, try again\n")

main()