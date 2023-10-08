import numpy as np

# Transition probability matrix
P = np.array([[1/12, 5/12, 1/2],
              [1/12, 5/12, 1/2],
              [0, 1, 0]])  # Absorbing state

# Calculate the fundamental matrix (N)
N = np.linalg.inv(np.eye(2) - P[:2, :2])

# Probability of reaching the absorbing state from state 1
probability_to_absorbing_state = N[0, 0]

print(f"Probability of eventually having no users: {probability_to_absorbing_state:.4f}")
