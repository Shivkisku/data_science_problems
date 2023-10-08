# ABTest_SignupIncreaseAnalysis.py

import numpy as np
import scipy.stats as stats

# Sample data (signup rates for control and experimental groups)
control_group = np.array([0.1, 0.15, 0.12, 0.08, 0.09])
experimental_group = np.array([0.18, 0.2, 0.22, 0.15, 0.17])

# Perform an independent two-sample t-test
t_stat, p_value = stats.ttest_ind(control_group, experimental_group)

# Set the significance level (e.g., 0.05)
alpha = 0.05

# Check if the p-value is less than the significance level
if p_value < alpha:
    print("The new feature significantly increases signups.")
else:
    print("There is no significant difference in signups between the groups.")
