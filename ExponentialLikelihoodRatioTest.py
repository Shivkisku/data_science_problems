import numpy as np

def likelihood_exponential(lmbda, data):
    # Calculate the likelihood for exponential distribution
    return np.prod(lmbda * np.exp(-lmbda * data))

def likelihood_ratio_test(data, lmbda0, lmbda1):
    # Calculate likelihoods under H0 and H1
    likelihood_H0 = likelihood_exponential(lmbda0, data)
    likelihood_H1 = likelihood_exponential(lmbda1, data)
    
    # Calculate the likelihood ratio
    likelihood_ratio = likelihood_H1 / likelihood_H0
    
    return likelihood_ratio

# Example usage:
data = np.array([1.2, 0.8, 2.5, 1.0, 1.6])
lambda0 = 0.5  # Null hypothesis rate parameter
lambda1 = 1.0  # Alternative hypothesis rate parameter

lr = likelihood_ratio_test(data, lambda0, lambda1)
print(f"Likelihood Ratio: {lr:.4f}")
