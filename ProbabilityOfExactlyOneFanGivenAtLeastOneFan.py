# Probability that a person is a fan
P_fan = 0.5

# Probability of having exactly one fan in a group of three
P_exactly_one_fan = 3 * P_fan * (1 - P_fan) * (1 - P_fan)

# Probability that there is at least one fan among the three
P_at_least_one_fan = 1 - (1 - P_fan)**3

# Probability of having exactly one fan given that there is at least one fan
P_given_at_least_one_fan = P_exactly_one_fan / P_at_least_one_fan

print(f"The probability of having exactly one fan, given that there is a fan among the three, is: {P_given_at_least_one_fan:.4f}")
