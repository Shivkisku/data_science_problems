import numpy as np
import scipy.stats as stats

# Parameters for the model's estimate distribution
true_score_mean = 92  # Mean of the true credit score
calibration_error_stddev = 1  # Standard deviation of the calibration error

# Number of samples to generate
num_samples = 100000

# Generate random samples from a normal distribution representing model estimates
model_estimates = np.random.normal(loc=true_score_mean, scale=calibration_error_stddev, size=num_samples)

# Define the cutoff for considering individuals credit-worthy
cutoff = 92

# Calculate the proportion of individuals who are considered credit-worthy
proportion_credit_worthy = np.mean(model_estimates >= cutoff)

# Check if we are overestimating or underestimating
if proportion_credit_worthy > 0.5:
    estimation_bias = "overestimating"
else:
    estimation_bias = "underestimating"

# Print the results
print(f"We are {estimation_bias} the actual population's credit score.")
print(f"Proportion considered credit-worthy: {proportion_credit_worthy:.2%}")
