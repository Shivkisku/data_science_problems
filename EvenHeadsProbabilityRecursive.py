# EvenHeadsProbabilityRecursive.py

def probability_even_heads(n, k, p, memo):
    # Base cases
    if k < 0:
        return 0
    if n == 0:
        return 1 if k == 0 else 0
    
    # Check if the result is memoized
    if (n, k) in memo:
        return memo[(n, k)]
    
    # Calculate the probability using the recurrence relation
    result = p * probability_even_heads(n-1, k-1, p, memo) + (1-p) * probability_even_heads(n-1, k, p, memo)
    
    # Memoize the result
    memo[(n, k)] = result
    
    return result

# Example usage:
n = 4  # Number of tosses
k = 2  # Number of heads
p = 0.5  # Probability of heads

memo = {}  # Memoization dictionary
result = probability_even_heads(n, k, p, memo)
print(f"The probability of getting {k} heads in {n} tosses is {result}")
