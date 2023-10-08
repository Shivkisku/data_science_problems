import numpy as np

# Generate some example data
np.random.seed(0)
X = np.random.rand(100)
Y = 2 * X + 1 + np.random.randn(100)  # Linear relationship with noise

# Fit a linear regression model
coefficients = np.polyfit(X, Y, 1)

# Calculate RSS (sum of squared residuals)
residuals = Y - (coefficients[0] * X + coefficients[1])
RSS = np.sum(residuals ** 2)

print(f"Coefficients: {coefficients}")
print(f"RSS (Sum of Squared Residuals): {RSS}")
