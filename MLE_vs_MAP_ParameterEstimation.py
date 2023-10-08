# MLE_vs_MAP_ParameterEstimation.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate synthetic data from a Gaussian distribution
np.random.seed(0)
data = np.random.normal(3, 1, 100)

# MLE estimation
mu_mle, std_mle = norm.fit(data)
pdf_mle = norm.pdf(data, mu_mle, std_mle)

# MAP estimation with a prior belief
prior_mu = 2.5
prior_std = 0.5
pdf_prior = norm.pdf(data, prior_mu, prior_std)
pdf_map = pdf_prior * pdf_mle  # Incorporate prior

# Plot the results
plt.hist(data, bins=20, density=True, alpha=0.6, color='b', label='Data Histogram')
plt.plot(data, pdf_mle, 'r-', lw=2, label='MLE Fit')
plt.plot(data, pdf_map, 'g-', lw=2, label='MAP Fit (with Prior)')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.legend()
plt.title('MLE vs. MAP Parameter Estimation')
plt.show()
