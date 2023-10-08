import numpy as np
import matplotlib.pyplot as plt

# Define the range of radii (0 to 1) and the corresponding PDF values
radii = np.linspace(0, 1, 1000)
pdf_radii = np.ones_like(radii)  # The PDF of the radius is constant (1) over the range [0, 1]

# Calculate the corresponding areas and PDF values
areas = np.pi * radii**2
pdf_areas = 2 * np.pi * radii  # Derivative of the CDF of the area

# Plot the PDF of the area
plt.figure(figsize=(8, 6))
plt.plot(areas, pdf_areas, label='PDF of Area')
plt.xlabel('Area')
plt.ylabel('PDF')
plt.title('Probability Density Function of Circle Area')
plt.grid(True)
plt.legend()
plt.show()
