# Define the prior probabilities
P_A = 0.5  # Probability of picking the fair coin
P_B = 0.5  # Probability of picking the unfair coin

# Define the probabilities of getting 5 consecutive tails for each coin
P_T5_given_A = (0.5) ** 5  # Probability of 5 consecutive tails with the fair coin
P_T5_given_B = 1.0  # Probability of 5 consecutive tails with the unfair coin

# Calculate the probability of picking the unfair coin given 5 consecutive tails
P_B_given_T5 = (P_B * P_T5_given_B) / (P_A * P_T5_given_A + P_B * P_T5_given_B)

# Print the result
print(f"The probability of picking the unfair coin given 5 consecutive tails is approximately {P_B_given_T5:.4f}")
