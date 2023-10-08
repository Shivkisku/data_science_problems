import numpy as np
from scipy.optimize import minimize

# Generate n random samples from the uniform distribution U(a, b)
n = 100
samples = np.random.uniform(2, 8, n)

# Define the likelihood function
def likelihood(params):
    a, b = params
    if a < b:
        return -n * np.log(b - a)
    else:
        return np.inf  # Return infinity if a >= b to enforce the constraint

# Find the MLE estimates of a and b
initial_guess = [np.min(samples), np.max(samples)]
result = minimize(likelihood, initial_guess, bounds=[(np.min(samples), np.max(samples)), (np.min(samples), np.max(samples))])

mle_a, mle_b = result.x

print(f"MLE estimate of 'a': {mle_a}")
print(f"MLE estimate of 'b': {mle_b}")
