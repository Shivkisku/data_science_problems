# calculate_covariance.py

import numpy as np

# Define the range for X
X_min = -1
X_max = 1

# Number of samples
num_samples = 100000

# Generate random samples for X
X = np.random.uniform(X_min, X_max, num_samples)

# Calculate Y = X^2
Y = X**2

# Calculate the expected values
E_X = np.mean(X)
E_Y = np.mean(Y)
E_XY = np.mean(X * Y)

# Calculate the covariance
covariance = E_XY - E_X * E_Y

print("Covariance between X and Y:", covariance)
