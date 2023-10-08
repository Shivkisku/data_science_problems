# RegularizationComparison.py

import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression, Lasso, Ridge
import matplotlib.pyplot as plt

# Generate synthetic data
X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=0)

# Create models with different types of regularization
linear_reg = LinearRegression()
lasso_reg = Lasso(alpha=1.0)  # L1 regularization
ridge_reg = Ridge(alpha=1.0)  # L2 regularization

# Fit the models to the data
linear_reg.fit(X, y)
lasso_reg.fit(X, y)
ridge_reg.fit(X, y)

# Plot the results
plt.figure(figsize=(10, 6))

# Plot data points
plt.scatter(X, y, label='Data', color='blue')

# Plot linear regression line
plt.plot(X, linear_reg.predict(X), label='Linear Regression', color='green')

# Plot L1 regularization (lasso) line
plt.plot(X, lasso_reg.predict(X), label='L1 Regularization (Lasso)', color='red')

# Plot L2 regularization (ridge) line
plt.plot(X, ridge_reg.predict(X), label='L2 Regularization (Ridge)', color='purple')

plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear vs. L1 vs. L2 Regularization')
plt.legend()
plt.grid(True)
plt.show()
