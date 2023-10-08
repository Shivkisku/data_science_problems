# Probability distribution for a fair 6-sided die
P = [1/6] * 6

# Calculate expected value for Game 1 (Two Dice - Product)
expected_value_game1 = sum(i * j * P[i-1] * P[j-1] for i in range(1, 7) for j in range(1, 7))

# Calculate expected value for Game 2 (One Die - Square)
expected_value_game2 = sum(i**2 * P[i-1] for i in range(1, 7))

# Compare expected values
if expected_value_game1 > expected_value_game2:
    print("Game 1 (Two Dice - Product) has the higher expected value.")
elif expected_value_game1 < expected_value_game2:
    print("Game 2 (One Die - Square) has the higher expected value.")
else:
    print("Both games have the same expected value.")
