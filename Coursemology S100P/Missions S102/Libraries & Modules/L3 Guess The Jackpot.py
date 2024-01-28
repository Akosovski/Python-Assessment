import random

def guessJackpot():
    number = random.randint(1, 10)
    chances = 5
    answer = 0

    while answer != number:
        if chances == 0:
            print("You lose.")
        else:
            answer = int(input(""))
            if answer > number:
                chances -= 1
                print("Between 1 to " + str(answer))
            elif answer < number:
                chances -= 1
                print("Between " + str(answer) + " to 10")
            elif answer == number:
                print("You win!")

guessJackpot()