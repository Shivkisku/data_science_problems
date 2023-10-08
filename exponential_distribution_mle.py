import numpy as np
from scipy.optimize import minimize

# Lifetime history (in months) of n customers
lifetime_data = np.array([10, 12, 8, 15, 20, 5, 18, 14, 9, 11])

# Define the negative log-likelihood function (to minimize)
def negative_log_likelihood(params):
    # params[0] contains lambda (rate parameter)
    lambda_ = params[0]
    return -np.sum(np.log(lambda_) - lambda_ * lifetime_data)

# Initial guess for lambda
initial_lambda = 1.0

# Minimize the negative log-likelihood to find MLE for lambda
result = minimize(negative_log_likelihood, [initial_lambda], method='L-BFGS-B')

# Extract the MLE for lambda from the optimization result
mle_lambda = result.x[0]

print(f"MLE for lambda: {mle_lambda:.4f}")
