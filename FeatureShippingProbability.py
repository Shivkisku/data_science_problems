# FeatureShippingProbability.py

# Probability that a single user likes the feature
p_single_user = 950 / 1000

# Probability that all 5 users like the feature (independent events)
p_all_users_like_feature = p_single_user ** 5

# Print the probability
print(f"Probability of shipping the feature: {p_all_users_like_feature:.4f}")
