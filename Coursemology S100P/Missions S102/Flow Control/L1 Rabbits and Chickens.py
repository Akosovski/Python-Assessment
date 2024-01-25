def rabbitChicken(heads, legs):
    if legs % 2 != 0 or heads > legs / 2 or heads < (legs - 4 * heads) / 2:
        return "No solution"

    # Calculate the number of chickens and rabbits
    chickens = (legs - 2 * heads) / 2
    rabbits = heads - chickens

    return f"{int(chickens)} {int(rabbits)}"

print(rabbitChicken(7, 22))