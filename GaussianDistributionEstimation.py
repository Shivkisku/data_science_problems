import numpy as np

# Replace this with your actual dataset
observations = [2.5, 3.0, 2.7, 3.2, 2.8, 3.5, 3.1, 2.9]

# Calculate the sample mean (μ_hat)
sample_mean = np.mean(observations)

# Calculate the sample standard deviation (σ_hat)
sample_stddev = np.std(observations)

print(f"Estimated Mean (μ_hat): {sample_mean:.4f}")
print(f"Estimated Standard Deviation (σ_hat): {sample_stddev:.4f}")
