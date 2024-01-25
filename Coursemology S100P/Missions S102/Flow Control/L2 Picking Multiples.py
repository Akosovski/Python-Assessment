def multiple_chance(): 
    favorable_outcomes = 0
    total_outcomes = 0

    # Iterate through all possible pairs of integers from 1 to 9
    for num1 in range(1, 10):
        for num2 in range(1, 10):
            # Count the total outcomes
            total_outcomes += 1

            # Check if one is a multiple of the other
            if num1 % num2 == 0 or num2 % num1 == 0:
                favorable_outcomes += 1

    # Calculate the probability
    probability = favorable_outcomes / total_outcomes

    return probability

print(multiple_chance())