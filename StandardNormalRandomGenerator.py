# StandardNormalRandomGenerator.py

import math
import random

def generate_standard_normal():
    u1 = random.random()  # Generate a random number from a uniform distribution [0, 1)
    u2 = random.random()  # Generate a second random number from a uniform distribution [0, 1)

    # Use the Box-Muller transform to generate two independent standard normal random variables
    z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
    z1 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)

    return z0

# Generate and print 10 random values from a standard normal distribution
for _ in range(10):
    value = generate_standard_normal()
    print(value)
