import numpy as np
import matplotlib.pyplot as plt

# Rate parameters for the faster and slower servers
lambda1 = 0.2  # Adjust as needed
lambda2 = 0.1  # Adjust as needed

# Define the time values for the PDF calculation
t_values = np.linspace(0, 20, 1000)  # Adjust the range as needed

# Calculate the PDF values
pdf_values = 0.5 * lambda1 * np.exp(-lambda1 * t_values) + 0.5 * lambda2 * np.exp(-lambda2 * t_values)

# Plot the PDF
plt.figure(figsize=(8, 6))
plt.plot(t_values, pdf_values, label='PDF of Waiting Time')
plt.xlabel('Waiting Time (t)')
plt.ylabel('PDF')
plt.title('Probability Density Function of Waiting Time')
plt.grid(True)
plt.legend()
plt.show()
