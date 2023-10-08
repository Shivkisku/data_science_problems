import numpy as np
import matplotlib.pyplot as plt

# Generate a synthetic dataset
np.random.seed(0)
x = np.random.rand(100)
y = np.sin(2 * np.pi * x) + 0.1 * np.random.randn(100)

# Kernel function (Gaussian kernel)
def gaussian_kernel(u):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * u**2)

# Kernel regression estimator function
def kernel_regression(x, y, x_query, bandwidth):
    n = len(x)
    total_weighted_sum = 0
    total_weight = 0
    
    for i in range(n):
        u = (x_query - x[i]) / bandwidth
        weight = gaussian_kernel(u)
        total_weighted_sum += weight * y[i]
        total_weight += weight
    
    return total_weighted_sum / total_weight if total_weight > 0 else 0

# Generate points for estimation
x_query = np.linspace(0, 1, 100)

# Bandwidth parameter
bandwidth = 0.1

# Compute the kernel regression estimates
y_estimates = [kernel_regression(x, y, xq, bandwidth) for xq in x_query]

# Plot the original data and kernel regression estimates
plt.scatter(x, y, label='Data', color='blue', alpha=0.5)
plt.plot(x_query, y_estimates, label='Kernel Regression', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Kernel Regression Estimation')
plt.show()
