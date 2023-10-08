# ab_test_driver_app.py

import numpy as np
from scipy import stats

# Generate sample data (replace this with your actual data)
np.random.seed(0)
control_group = np.random.randint(10, 20, size=100)  # Original app users
experimental_group = np.random.randint(15, 25, size=100)  # New app users

# Perform a two-sample t-test
t_stat, p_value = stats.ttest_ind(control_group, experimental_group)

# Set the significance level (alpha)
alpha = 0.05

# Check if the p-value is less than alpha
if p_value < alpha:
    print("Reject the null hypothesis: The new app increases the number of rides taken.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the apps.")
