# FraudDetectionThresholdAnalysis.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Simulate classifier scores (replace this with your actual classifier's scores)
np.random.seed(0)
scores = np.random.rand(100)

# Set a decision threshold (adjust as needed)
threshold = 0.5

# Simulate true labels (0: not fraudulent, 1: fraudulent)
true_labels = np.random.randint(2, size=100)

# Apply the decision threshold to classify predictions
predicted_labels = (scores > threshold).astype(int)

# Calculate the confusion matrix
conf_matrix = confusion_matrix(true_labels, predicted_labels)

# Calculate false positives and false negatives
false_positives = conf_matrix[0, 1]
false_negatives = conf_matrix[1, 0]

print(f"False Positives: {false_positives}")
print(f"False Negatives: {false_negatives}")

# Visualize the decision threshold and trade-offs
thresholds = np.linspace(0, 1, 100)
fp_rates = []
fn_rates = []

for th in thresholds:
    predicted_labels = (scores > th).astype(int)
    conf_matrix = confusion_matrix(true_labels, predicted_labels)
    fp_rate = conf_matrix[0, 1] / (conf_matrix[0, 0] + conf_matrix[0, 1])
    fn_rate = conf_matrix[1, 0] / (conf_matrix[1, 0] + conf_matrix[1, 1])
    fp_rates.append(fp_rate)
    fn_rates.append(fn_rate)

plt.figure(figsize=(8, 6))
plt.plot(thresholds, fp_rates, label="False Positive Rate (FP)")
plt.plot(thresholds, fn_rates, label="False Negative Rate (FN)")
plt.xlabel("Decision Threshold")
plt.ylabel("Rate")
plt.legend()
plt.title("Trade-offs between FP and FN Rates")
plt.show()
