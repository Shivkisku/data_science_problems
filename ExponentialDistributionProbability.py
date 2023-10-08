import math

def exponential_probability(mu, x):
    # Calculate the probability density function for exponential distribution
    pdf = (1 / mu) * math.exp(-x / mu)
    
    return pdf

def probability_wait_no_more_than_x(mu, x):
    # Calculate the cumulative probability up to x
    cumulative_prob = 1 - math.exp(-x / mu)
    
    return cumulative_prob

# Parameters
mean_wait_time = 10  # Mean wait time in minutes
current_wait_time = 5  # Current wait time for the customer in minutes

# Calculate the probability that the current customer will wait no more than another 5 minutes
probability = probability_wait_no_more_than_x(mean_wait_time, current_wait_time)

print(f"The probability that the customer will wait no more than another {current_wait_time} minutes is approximately {probability:.4f}")
