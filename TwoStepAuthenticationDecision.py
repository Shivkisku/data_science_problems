# TwoStepAuthenticationDecision.py

import random

# Simulated data
# You should replace this with actual data from your system and users
total_users = 1000  # Total number of users
users_with_2fa = 250  # Number of users who already have 2FA enabled
users_without_2fa = total_users - users_with_2fa  # Number of users without 2FA

# Simulated login attempts data
login_attempts_without_2fa = [random.randint(0, 5) for _ in range(users_without_2fa)]
login_attempts_with_2fa = [random.randint(0, 5) for _ in range(users_with_2fa)]

# Calculate login success rates
success_rate_without_2fa = sum(1 for attempts in login_attempts_without_2fa if attempts == 0) / users_without_2fa
success_rate_with_2fa = sum(1 for attempts in login_attempts_with_2fa if attempts == 0) / users_with_2fa

# Analyze the data and make a decision
if success_rate_without_2fa > success_rate_with_2fa:
    decision = "Implementing 2-step authentication may be beneficial."
else:
    decision = "Implementing 2-step authentication may not be necessary at this time."

# Print the decision and relevant data
print("Total Users:", total_users)
print("Users with 2FA:", users_with_2fa)
print("Users without 2FA:", users_without_2fa)
print("Success Rate without 2FA:", success_rate_without_2fa)
print("Success Rate with 2FA:", success_rate_with_2fa)
print("Decision:", decision)
