# Calculate the conditional expected value of X given X > Y
def conditional_expected_value():
    numerator = 0.0
    denominator = 0.5

    for x in range(1, 1001):  # Use numerical integration with step size 0.001
        x_value = x / 1000.0  # Convert to float
        numerator += x_value * x_value / 2.0  # Integrate with respect to y from 0 to x

    conditional_expectation = numerator / denominator
    return conditional_expectation

# Calculate and print the result
result = conditional_expected_value()
print(f"The conditional expected value of X given X > Y is: {result:.4f}")
