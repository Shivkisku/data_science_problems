import scipy.integrate as spi

# Define the function to integrate
def min_function(x, y):
    return min(x, y)

# Perform the double integral
expected_value, _ = spi.dblquad(min_function, 0, 1, lambda x: 0, lambda x: 1)

print(f"Expected value of min(X, Y): {expected_value:.4f}")
