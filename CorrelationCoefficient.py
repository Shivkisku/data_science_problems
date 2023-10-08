def correlation_coefficient(X, Y):
    # Calculate the expected values
    n = len(X)
    p_X = 1/6  # Probability of rolling a 2 on a fair six-sided die
    p_Y = 1/6  # Probability of rolling a 3 on a fair six-sided die
    p_XY = p_X * p_Y  # Joint probability of rolling both a 2 and a 3
    
    E_X = n * p_X
    E_Y = n * p_Y
    E_XY = n * p_XY
    
    # Calculate the covariance
    cov_XY = E_XY - E_X * E_Y
    
    # Calculate the standard deviations
    var_X = n * p_X * (1 - p_X)
    var_Y = n * p_Y * (1 - p_Y)
    
    std_X = var_X**0.5
    std_Y = var_Y**0.5
    
    # Calculate the correlation coefficient
    correlation = cov_XY / (std_X * std_Y)
    
    return correlation

# Example usage:
X = [0, 1, 2, 3, 4, 5]  # Possible values for X (number of times a 2 was rolled)
Y = [0, 1, 2, 3, 4, 5]  # Possible values for Y (number of times a 3 was rolled)

corr_coefficient = correlation_coefficient(X, Y)
print(f"The correlation coefficient between X and Y is approximately {corr_coefficient:.4f}")
