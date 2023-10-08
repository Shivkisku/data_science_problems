import numpy as np
from sklearn.mixture import GaussianMixture

# Sample data for training
data = np.random.randn(100, 2)

# Train a Gaussian Mixture Model (GMM)
n_components = 2
gmm = GaussianMixture(n_components=n_components, random_state=0)
gmm.fit(data)

# New transaction for evaluation
new_transaction = np.array([[1.0, -1.0]])  # Replace with your transaction data

# Calculate the log likelihood of the new transaction
log_likelihood = gmm.score_samples(new_transaction)

# Set a decision threshold (you can adjust this)
threshold = -5.0

# Determine if the transaction is fraudulent or not
if log_likelihood < threshold:
    print("Transaction is likely fraudulent.")
else:
    print("Transaction is likely non-fraudulent.")
