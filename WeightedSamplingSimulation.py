import random

def weighted_sample(categories, weights, total_items):
    for _ in range(total_items):
        sampled_category = random.choices(categories, weights=weights, k=1)[0]
        yield sampled_category

# Define the categories and their corresponding weights
categories = ["A", "B", "C", "D"]
weights = [0.20, 0.15, 0.35, 0.30]

# Total number of items to sample
total_items = 100

# Simulate and print the results using a generator
category_counts = {category: 0 for category in categories}
for sampled_category in weighted_sample(categories, weights, total_items):
    category_counts[sampled_category] += 1

for category, count in category_counts.items():
    print(f"{category}: {count} ({count / total_items * 100:.2f}%)")
