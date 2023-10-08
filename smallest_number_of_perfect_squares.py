# smallest_number_of_perfect_squares.py

def numSquares(n):
    # Create a list to store the minimum number of squares needed for each value from 0 to n
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        # Initialize dp[i] to the maximum possible value, which is i
        dp[i] = i
        j = 1
        while j * j <= i:
            # Update dp[i] by considering all possible perfect squares
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[n]

# Test cases
print(numSquares(7))  # Output: 4 (7 = 4 + 1 + 1 + 1)
print(numSquares(13))  # Output: 2 (13 = 4 + 9)
