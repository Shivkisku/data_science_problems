# coin_unfairness_detection.py

import scipy.stats as stats

# Define the probability of heads for an unfair coin
p_heads_unfair = 0.6

# Define the significance level (alpha)
alpha = 0.05

# Calculate the number of coin flips needed to detect unfairness
n_flips_needed = 0
while True:
    n_flips_needed += 1
    # Calculate the probability of observing n_heads or more heads in n_flips
    p_value = 2 * min(stats.binom.cdf(n_flips_needed // 2, n_flips_needed, p_heads_unfair),
                     1 - stats.binom.cdf(n_flips_needed // 2 - 1, n_flips_needed, p_heads_unfair))
    
    if p_value < alpha:
        break

print("Number of coin flips needed to detect unfairness:", n_flips_needed)
