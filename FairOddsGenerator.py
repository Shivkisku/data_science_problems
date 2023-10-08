import random

# Function to simulate flipping the unfair coin
def flip_unfair_coin(probability_heads):
    return random.random() < probability_heads

# Simulate flipping the unfair coin multiple times
num_trials = 100000  # Adjust the number of trials as needed
bias_towards_heads = 0.6  # Adjust the bias as needed (e.g., 0.6 means 60% chance of heads)

head_count = 0
tail_count = 0

for _ in range(num_trials):
    if flip_unfair_coin(bias_towards_heads):
        head_count += 1
    else:
        tail_count += 1

# Calculate the fair odds
if head_count > tail_count:
    fair_odds_heads = 1.0
    fair_odds_tails = head_count / tail_count
else:
    fair_odds_heads = tail_count / head_count
    fair_odds_tails = 1.0

print(f"Fair odds for heads: {fair_odds_heads:.2f}")
print(f"Fair odds for tails: {fair_odds_tails:.2f}")
