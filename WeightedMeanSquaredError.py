# WeightedMeanSquaredError.py

import numpy as np

# Simulated data (replace with actual data)
actual_energy_consumption = np.array([100, 120, 95, 105, 110])  # Actual energy consumption values
predicted_energy_consumption = np.array([105, 118, 92, 100, 105])  # Predicted energy consumption values
sensor_reliability = np.array([0.9, 0.7, 0.5, 0.9, 0.2])  # Sensor reliability values (1.0 is perfect reliability)

# Calculate Weighted Mean Squared Error (WMSE)
error = actual_energy_consumption - predicted_energy_consumption
wmse = np.mean((error ** 2) * sensor_reliability)

print(f"Weighted Mean Squared Error (WMSE): {wmse}")
