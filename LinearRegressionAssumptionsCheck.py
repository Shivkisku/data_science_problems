# LinearRegressionAssumptionsCheck.py

import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

# Simulated data
X = np.random.rand(100)
y = 2 * X + 1 + np.random.normal(0, 1, 100)

# Fit a linear regression model
X = sm.add_constant(X)  # Add a constant term for the intercept
model = sm.OLS(y, X).fit()

# Check assumptions
residuals = model.resid

# 1. Linearity: Plot residuals vs. fitted values
plt.scatter(model.fittedvalues, residuals)
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.title('Linearity Check')
plt.show()

# 2. Independence of Errors: Use Durbin-Watson test
from statsmodels.stats.stattools import durbin_watson
dw_statistic = durbin_watson(residuals)
print(f"Durbin-Watson Statistic: {dw_statistic}")

# 3. Homoscedasticity: Plot residuals vs. predictor values
plt.scatter(X[:, 1], residuals)
plt.xlabel('Predictor')
plt.ylabel('Residuals')
plt.title('Homoscedasticity Check')
plt.show()

# 4. Normality of Residuals: Plot a histogram of residuals
plt.hist(residuals, bins=20)
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Normality Check')
plt.show()
