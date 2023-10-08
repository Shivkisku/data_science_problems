import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective(params, x, y):
    w, b, sigma = params
    predicted_y = w * x + b
    loss = 0.5 * np.log(2 * np.pi * sigma**2) + ((y - predicted_y)**2) / (2 * sigma**2)
    return np.sum(loss)

# Generate some sample data
np.random.seed(0)
x = np.random.rand(100)
y_true = 2 * x + 1
noise = np.random.normal(0, 0.5, 100)
y_observed = y_true + noise

# Initial guess for parameters
initial_params = [1.0, 0.0, 1.0]  # [w, b, sigma]

# Minimize the objective function
result = minimize(objective, initial_params, args=(x, y_observed))

# Extract the optimized parameters
w_opt, b_opt, sigma_opt = result.x

print(f"Optimized w: {w_opt}")
print(f"Optimized b: {b_opt}")
print(f"Optimized sigma: {sigma_opt}")
