# AntCollisionProbability.py

def probability_no_collision(k):
    total_outcomes = 2 ** k
    favorable_outcomes = 2  # All ants move in the same direction (clockwise or counterclockwise)
    
    for i in range(2, k + 1):
        # Use inclusion-exclusion principle to count combinations where i ants move in the same direction
        favorable_outcomes += (-1) ** i * (2 ** (k - i)) * comb(k, i)
    
    probability = favorable_outcomes / total_outcomes
    return probability

def comb(n, k):
    # Calculate binomial coefficient (n choose k)
    if 0 <= k <= n:
        result = 1
        for i in range(min(k, n - k)):
            result *= (n - i)
            result //= (i + 1)
        return result
    else:
        return 0

# Example usage:
k = 3
probability = probability_no_collision(k)
print(f"Probability of no collision for {k} ants: {probability}")
