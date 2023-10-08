# DieRollStatistics.py

import numpy as np

def expected_value(n):
    return (1/6) * sum(i * (i - 1) for i in range(1, 7))

def variance(n, e_min):
    return sum((i - e_min) ** 2 * (i - 1) / 6 for i in range(1, 7))

def standard_deviation(variance):
    return np.sqrt(variance)

n = 10  # Number of times the die is rolled
e_min = expected_value(n)
var = variance(n, e_min)
std_dev = standard_deviation(var)

print(f"Expected Value of the Smallest Number: {e_min:.2f}")
print(f"Standard Deviation of the Smallest Number: {std_dev:.2f}")
