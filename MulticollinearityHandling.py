import numpy as np
from sklearn.linear_model import Ridge
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Generate synthetic data with correlated predictors
X, y = make_regression(n_samples=100, n_features=5, noise=10, random_state=0)
X_correlated = X.copy()
X_correlated[:, 1] = X[:, 0] * 2  # Create correlation between features 0 and 1

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_correlated, y, test_size=0.2, random_state=0)

# Fit Ridge Regression model with regularization strength (alpha) to address multicollinearity
alpha = 1.0  # You can adjust this parameter
ridge = Ridge(alpha=alpha)
ridge.fit(X_train, y_train)

# Make predictions
y_pred = ridge.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error (Ridge Regression): {mse:.2f}")
