import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Number of simulations
num_simulations = 10000

# Initialize a list to store the number of days for each simulation
num_days_list = []

# Perform Monte Carlo simulation
for _ in range(num_simulations):
    num_days = 0
    while True:
        num_days += 1
        sample = np.random.normal(0, 1)
        if sample > 2:
            break
    num_days_list.append(num_days)

# Calculate the average number of days
average_num_days = np.mean(num_days_list)

print(f"Estimated expected number of days until X > 2: {average_num_days:.2f}")
