import random
import matplotlib.pyplot as plt

# Number of random points to generate
num_points = 1000

# Initialize counters for points inside the circle
inside_circle = 0

# Lists to store coordinates of points inside and outside the circle (for visualization)
x_inside = []
y_inside = []
x_outside = []
y_outside = []

# Generate random points and check if they are inside the circle
for _ in range(num_points):
    x = random.uniform(0, 1)  # Random x-coordinate in [0, 1]
    y = random.uniform(0, 1)  # Random y-coordinate in [0, 1]
    
    # Calculate the distance from the origin (0, 0)
    distance = x**2 + y**2
    
    # Check if the point is inside the unit circle
    if distance <= 1:
        inside_circle += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

# Estimate π using Monte Carlo method
pi_estimate = (inside_circle / num_points) * 4

# Plot the points inside and outside the circle for visualization
plt.figure(figsize=(6, 6))
plt.scatter(x_inside, y_inside, color='blue', s=5, label='Inside Circle')
plt.scatter(x_outside, y_outside, color='red', s=5, label='Outside Circle')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f'Estimation of π: {pi_estimate:.5f}')
plt.legend()
plt.show()

print(f'Estimated π: {pi_estimate:.5f}')
