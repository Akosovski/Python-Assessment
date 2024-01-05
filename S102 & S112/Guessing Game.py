import random
result = random.randint(1, 10)
guess = 0
tries = 0
while True:
    guess = int(input("What is your guess? "))
    if guess > result:
        tries += 1
        print("Too big!")
    elif guess < result:
        tries += 1
        print("Too small!")
    elif guess == result:
        tries += 1
        print("Correct!")
        print("You took " + str(tries) + " guesses.")
        break

