# BernoulliMLE.py

import numpy as np
from scipy.optimize import minimize

# Observed samples
samples = [1, 0, 1, 1, 1]

# Log-likelihood function for Bernoulli distribution
def log_likelihood(p):
    likelihood = np.sum([y * np.log(p) + (1 - y) * np.log(1 - p) for y in samples])
    return -likelihood  # Minimize the negative log-likelihood

# Initial guess for p (you can choose any reasonable initial value)
initial_guess = 0.5

# Optimization to find MLE of p
result = minimize(log_likelihood, initial_guess, method='Nelder-Mead')
mle_p = result.x[0]

print(f"Maximum Likelihood Estimate (MLE) of p: {mle_p:.4f}")
