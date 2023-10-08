import matplotlib.pyplot as plt
import numpy as np

# Simulated data (replace with actual data)
dates = ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05"]
dau = [10000, 9500, 9800, 9300, 9000]
wau = [25000, 24000, 24500, 23800, 23000]
mau = [75000, 73000, 74000, 72800, 72000]

sessions = [10, 9, 11, 9, 8]
session_lengths = [30, 32, 28, 30, 29]

# Calculate average actions per session and average session length
avg_actions_per_session = np.mean(sessions)
avg_session_length = np.mean(session_lengths)

# Calculate week-over-week and month-over-month growth rates
wow_growth = ((dau[-1] - dau[-2]) / dau[-2]) * 100
mom_growth = ((mau[-1] - mau[-2]) / mau[-2]) * 100

# Plot DAU, WAU, MAU over time
plt.figure(figsize=(10, 6))
plt.plot(dates, dau, label='DAU', marker='o')
plt.plot(dates, wau, label='WAU', marker='o')
plt.plot(dates, mau, label='MAU', marker='o')
plt.xlabel('Date')
plt.ylabel('Number of Users')
plt.title('User Engagement Metrics Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Print engagement metrics
print(f'Average Actions per Session: {avg_actions_per_session:.2f}')
print(f'Average Session Length (minutes): {avg_session_length:.2f}')
print(f'Week-over-Week Growth Rate: {wow_growth:.2f}%')
print(f'Month-over-Month Growth Rate: {mom_growth:.2f}%')

plt.show()
