# UncorrelatedButNotIndependent.py

import numpy as np

# Generate random data for X and Y
np.random.seed(0)
X = np.random.rand(100)  # Random values between 0 and 1
Y = X**2  # Y is a nonlinear transformation of X

# Calculate the covariance between X and Y
covariance = np.cov(X, Y)[0, 1]

print(f"Covariance between X and Y: {covariance:.4f}")
