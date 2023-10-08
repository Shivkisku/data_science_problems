import scipy.stats as stats

def probability_within_n(muX, sigmaX, muY, sigmaY, n):
    # Calculate the parameters of Z = X - Y
    muZ = muX - muY
    sigmaZ = (sigmaX ** 2 + sigmaY ** 2) ** 0.5

    # Standardize Z to a standard normal distribution
    z_score = n / sigmaZ

    # Calculate the probability P(|X - Y| ≤ n) using the standard normal CDF
    probability = stats.norm.cdf(z_score) - stats.norm.cdf(-z_score)

    return probability

# Example usage:
muX = 200000  # Mean of electric vehicle X's lifetime
sigmaX = 30000  # Standard deviation of electric vehicle X's lifetime
muY = 180000  # Mean of electric vehicle Y's lifetime
sigmaY = 25000  # Standard deviation of electric vehicle Y's lifetime
n = 10000  # Time units

probability = probability_within_n(muX, sigmaX, muY, sigmaY, n)
print(f"Probability that the two lifetimes are within {n} time units: {probability:.4f}")
