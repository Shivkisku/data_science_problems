import math

def calculate_probability(n, r):
    # Calculate the binomial coefficient C(n, r)
    num_ways = math.comb(n, r)
    
    # Calculate the probability
    probability = num_ways / (6 ** n)
    
    return probability

# Number of times the die is rolled
n = 3  # You can change this to any positive integer

# Calculate and print the probabilities for each 'r' from 1 to 6
for r in range(1, 7):
    probability = calculate_probability(n, r)
    print(f"Probability that max number is {r}: {probability:.4f}")
