# ClickingBehaviorVarianceComparison.py

import numpy as np
from scipy import stats

# Simulated data (replace with actual data from both countries)
clicks_country1 = np.array([15, 18, 20, 22, 25])  # Clicking behavior data for Country 1
clicks_country2 = np.array([12, 16, 19, 21, 23])  # Clicking behavior data for Country 2

# Perform the F-test for comparing variances
variance_country1 = np.var(clicks_country1, ddof=1)  # ddof=1 for sample variance
variance_country2 = np.var(clicks_country2, ddof=1)

# Calculate the F-statistic
F_statistic = variance_country1 / variance_country2

# Calculate the degrees of freedom
df1 = len(clicks_country1) - 1
df2 = len(clicks_country2) - 1

# Calculate the p-value
p_value = 2 * min(stats.f.cdf(F_statistic, df1, df2), 1 - stats.f.cdf(F_statistic, df1, df2))

# Define the significance level (alpha)
alpha = 0.05

# Make a decision based on the p-value and alpha
if p_value < alpha:
    result = "Reject null hypothesis: Variances are not equal"
else:
    result = "Fail to reject null hypothesis: Variances are equal"

# Print the results
print("Variance of Country 1:", variance_country1)
print("Variance of Country 2:", variance_country2)
print("F-statistic:", F_statistic)
print("Degrees of Freedom (df1, df2):", df1, df2)
print("P-value:", p_value)
print("Result:", result)
