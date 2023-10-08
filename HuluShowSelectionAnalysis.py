# Probability of selecting a show
p_selection = 1 / 50

# Calculate the expected number of common shows
expected_common_shows = p_selection

# Calculate the probability of having no shows in common
probability_no_common_shows = (49 / 50) * (48 / 49) * (47 / 48)

print(f"Expected Number of Common Shows: {expected_common_shows:.2f}")
print(f"Probability of Having No Shows in Common: {probability_no_common_shows:.2f}")
