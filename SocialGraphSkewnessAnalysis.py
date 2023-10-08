# SocialGraphSkewnessAnalysis.py

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Generate a hypothetical social graph for illustration
G = nx.erdos_renyi_graph(1000, 0.1)

# Calculate the degree of each node
degrees = [degree for _, degree in G.degree()]

# Calculate the Gini coefficient
def gini_coefficient(data):
    data = sorted(data)
    n = len(data)
    numer = 2 * np.sum([(i + 1) * data[i] for i in range(n)])
    denom = n * np.sum(data)
    return 1 - (numer / denom)

gini = gini_coefficient(degrees)

# Calculate the standard deviation of node degrees
std_dev = np.std(degrees)

# Plot the degree distribution
plt.hist(degrees, bins=30, density=True, alpha=0.7)
plt.xlabel('Node Degree')
plt.ylabel('Frequency')
plt.title('Degree Distribution')
plt.show()

# Print the metrics
print(f"Gini Coefficient: {gini:.4f}")
print(f"Standard Deviation of Node Degrees: {std_dev:.4f}")
