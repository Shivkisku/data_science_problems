import scipy.stats as stats

# Number of coin flips
n_flips = 1000

# Number of heads observed
n_heads_observed = 550

# Null hypothesis: The coin is fair (not biased)
p_null = 0.5  # Probability of heads in a fair coin

# Perform the binomial test
p_value = stats.binom_test(n_heads_observed, n_flips, p_null)

# Set the significance level (alpha)
alpha = 0.05

# Determine whether to reject the null hypothesis
if p_value < alpha:
    print("Reject the null hypothesis. The coin is likely biased.")
else:
    print("Fail to reject the null hypothesis. There is no strong evidence that the coin is biased.")
