import numpy as np

# Sample data points and initial cluster centroids
X = np.array([[1, 2], [2, 3], [3, 4], [8, 9], [9, 10]])
centroids = np.array([[1.0, 2.0], [8.0, 9.0]])  # Use float64 data type
learning_rate = 0.01

# Batch Gradient Descent Update for Centroids
def batch_gradient_descent(X, centroids):
    assignments = np.argmin(np.linalg.norm(X[:, np.newaxis] - centroids, axis=2), axis=1)
    new_centroids = np.array([X[assignments == k].mean(axis=0) for k in range(centroids.shape[0])])
    return new_centroids

# Stochastic Gradient Descent Update for Centroids
def stochastic_gradient_descent(X, centroids, learning_rate):
    i = np.random.randint(X.shape[0])
    x_i = X[i]
    assignments = np.argmin(np.linalg.norm(x_i - centroids, axis=1))
    centroids[assignments] += learning_rate * (x_i - centroids[assignments])
    return centroids

# Batch Gradient Descent Update
new_centroids_batch = batch_gradient_descent(X, centroids)

# Stochastic Gradient Descent Update
new_centroids_stochastic = stochastic_gradient_descent(X, centroids, learning_rate)

print("Batch Gradient Descent Update:")
print(new_centroids_batch)

print("\nStochastic Gradient Descent Update:")
print(new_centroids_stochastic)
