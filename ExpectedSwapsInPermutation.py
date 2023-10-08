def derangements(n):
    # Base cases
    if n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize derangements for n = 1 and n = 2
    d_prev = 0
    d_current = 1

    for i in range(3, n + 1):
        # Calculate derangements using the recursive formula
        d_next = (i - 1) * (d_current + d_prev)
        
        # Update derangements for the next iteration
        d_prev, d_current = d_current, d_next

    return d_current

def expected_swaps(n):
    # Calculate the expected number of swaps as n - D(n)
    return n - derangements(n)

# Example usage
n = 5  # Number of integers 1...n
expected_swaps_result = expected_swaps(n)
print(f"Expected number of swaps for {n} integers: {expected_swaps_result}")
