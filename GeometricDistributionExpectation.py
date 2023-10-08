def geometric_mean(p):
    # Initialize the expectation to 0
    expectation = 0
    
    # Iterate through all possible values of k
    for k in range(1, 1001):  # Assume precision up to 3 decimal places
        probability = ((1 - p) ** (k - 1)) * p
        expectation += k * probability
    
    return expectation

# Example usage:
p = 0.2  # Probability of success
result = geometric_mean(p)
print(f"The expectation (mean) of the geometric distribution with p={p} is approximately {result:.4f}")
