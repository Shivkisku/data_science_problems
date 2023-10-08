from itertools import combinations

def calculate_probability():
    # Define the number of sides on a die
    sides = 6

    # Generate all possible combinations of three different dice rolls
    all_combinations = list(combinations(range(1, sides + 1), 3))

    # Initialize a counter for favorable outcomes
    favorable_outcomes = 0

    # Count the number of favorable outcomes (sums to 12)
    for combo in all_combinations:
        if sum(combo) == 12:
            favorable_outcomes += 1

    # Calculate the total number of possible outcomes
    total_outcomes = len(all_combinations)

    # Calculate the probability
    probability = favorable_outcomes / total_outcomes

    return probability

# Calculate and print the probability
result = calculate_probability()
print(f"The probability of rolling a sum of 12 with three different dice is: {result:.4f}")
