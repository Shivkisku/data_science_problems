# UncorrelationCheck.py

import numpy as np

# Simulated data (replace with actual data or distributions)
np.random.seed(0)
X = np.random.rand(100)  # Random data for X
Y = np.random.rand(100)  # Random data for Y

# Calculate the means
mean_X = np.mean(X)
mean_Y = np.mean(Y)

# Calculate covariance between X and Y
covariance = np.cov(X, Y)[0, 1]

# Check if X + Y and X - Y are uncorrelated
uncorrelated = covariance == 0

# Print the results
print("Covariance between X and Y:", covariance)
if uncorrelated:
    print("X + Y and X - Y are uncorrelated.")
else:
    print("X + Y and X - Y are not uncorrelated.")
