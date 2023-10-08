import numpy as np

def calculate_long_term_frequency(p, n):
    # Create the transition probability matrix
    transition_matrix = np.array([[1 - p, p], [0, 1]])

    # Define the initial state distribution (all vehicles start in the operational state)
    initial_state = np.array([1, 0])

    # Calculate the long-term frequency of replacements using the limiting distribution
    limiting_distribution = initial_state
    for _ in range(n - 1):
        limiting_distribution = np.dot(limiting_distribution, transition_matrix)

    # The long-term frequency of replacements is the probability of being in the "Replacement Required" state
    frequency_of_replacements = limiting_distribution[1]

    return frequency_of_replacements

# Example parameters
p = 0.01  # Probability of malfunction or crash
n = 30    # Number of days a vehicle can be around before replacement

# Calculate the long-term frequency of replacements
frequency = calculate_long_term_frequency(p, n)
print(f"Long-term frequency of vehicle replacements: {frequency:.4f}")
