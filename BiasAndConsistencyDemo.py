import numpy as np
import matplotlib.pyplot as plt

# Generate random data from a normal distribution with mean 5 and standard deviation 2
np.random.seed(0)
true_mean = 5
data = np.random.normal(true_mean, 2, size=1000)

# Calculate sample means for different sample sizes
sample_sizes = np.arange(1, 1001)
sample_means = [np.mean(data[:n]) for n in sample_sizes]

# Calculate bias and plot it
bias = [mean - true_mean for mean in sample_means]
plt.plot(sample_sizes, bias)
plt.xlabel('Sample Size')
plt.ylabel('Bias')
plt.title('Bias of Sample Mean')
plt.show()
