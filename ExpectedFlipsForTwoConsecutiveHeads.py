import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Number of simulations
num_simulations = 10000

# Initialize a list to store the number of flips for each simulation
num_flips_list = []

# Perform Monte Carlo simulation
for _ in range(num_simulations):
    num_flips = 0
    consecutive_heads = 0
    while consecutive_heads < 2:
        num_flips += 1
        outcome = np.random.randint(2)  # 0 for tails, 1 for heads
        if outcome == 1:
            consecutive_heads += 1
        else:
            consecutive_heads = 0  # Reset if tails appears
    num_flips_list.append(num_flips)

# Calculate the average number of flips
average_num_flips = np.mean(num_flips_list)

print(f"Estimated expected number of flips to get two consecutive heads: {average_num_flips:.2f}")
