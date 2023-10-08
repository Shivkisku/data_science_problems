# Simulated demand and supply metrics
demand = 100  # Simulated passenger demand
available_drivers = 80  # Number of available drivers
surge_multiplier = 1.0  # Initial surge pricing multiplier

# Adjust surge pricing based on demand and supply
if demand > available_drivers:
    shortage_ratio = demand / available_drivers
    if shortage_ratio > 1.5:
        surge_multiplier = 2.0  # Apply a high surge multiplier for severe shortages
    else:
        surge_multiplier = 1.5  # Apply a moderate surge multiplier

print(f"Surge pricing multiplier: {surge_multiplier}")
