def probability_bob_wins(p, n):
    q = 1 - p  # Probability that Bob wins a round

    # Probability of Bob winning in exactly n rounds
    bob_wins_n_rounds = q**n

    # Probability of series continuing beyond n rounds
    series_continues = sum(p**i * q**i for i in range(n + 2, 1000))  # Assuming a maximum of 1000 rounds

    # Total probability that Bob wins
    probability_bob_wins = bob_wins_n_rounds + series_continues

    return probability_bob_wins

# Example usage
p = 0.4  # Probability that Alice wins a round
n = 2    # Number of rounds needed for one player to win two more rounds than the other

result = probability_bob_wins(p, n)
print(f"Probability that Bob wins the series: {result:.4f}")
