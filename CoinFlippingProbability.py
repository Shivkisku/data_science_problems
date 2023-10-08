# CoinFlippingProbability.py

import math

def probability_more_heads(n):
    total_outcomes = 2 ** (n + n + 1)  # Total possible outcomes when flipping all coins
    favorable_outcomes = 0

    # Calculate the number of favorable outcomes
    for k in range(n + 2):  # A can have 0 to n+1 heads
        favorable_outcomes += math.comb(n + 1, k) * math.comb(n, n + 1 - k)

    # Probability is the ratio of favorable outcomes to total outcomes
    probability = favorable_outcomes / total_outcomes
    return probability

# Example usage:
n = 3  # Number of coins A has
result = probability_more_heads(n)
print(f"Probability that A has more heads than B: {result:.4f}")
