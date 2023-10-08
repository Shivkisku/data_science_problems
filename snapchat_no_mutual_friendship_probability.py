def derangement(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    return (n - 1) * (derangement(n - 1) + derangement(n - 2))

def probability_no_mutual_friendships(n):
    total_pairings = factorial(n)
    derangements = derangement(n)
    probability = derangements / total_pairings
    return probability

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Number of users in each group
n = 5  # You can change this to any positive integer

# Calculate the probability of no mutual best friendships
probability = probability_no_mutual_friendships(n)
print(f"Probability of no mutual best friendships for {n} users: {probability:.6f}")
