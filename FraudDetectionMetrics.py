# FraudDetectionMetrics.py

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score

# Simulated data (replace with your actual data)
actual_labels = [1, 0, 0, 1, 1, 0, 0, 1, 1, 1]  # Actual labels (1 for fraud, 0 for non-fraud)
predicted_labels = [1, 0, 1, 1, 0, 0, 0, 1, 1, 0]  # Predicted labels

# Calculate various metrics
accuracy = accuracy_score(actual_labels, predicted_labels)
precision = precision_score(actual_labels, predicted_labels)
recall = recall_score(actual_labels, predicted_labels)
f1 = f1_score(actual_labels, predicted_labels)
conf_matrix = confusion_matrix(actual_labels, predicted_labels)
roc_auc = roc_auc_score(actual_labels, predicted_labels)

# Print the results
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-Score: {f1}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"ROC AUC Score: {roc_auc}")
