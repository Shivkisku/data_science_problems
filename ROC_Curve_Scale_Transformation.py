# ROC_Curve_Scale_Transformation.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# Generate example probabilities from a classifier
np.random.seed(0)
y_true = np.random.randint(2, size=1000)  # True labels (0 or 1)
y_scores = np.random.rand(1000)  # Example classifier scores (between 0 and 1)

# Calculate ROC curve for the original scores
fpr_original, tpr_original, _ = roc_curve(y_true, y_scores)
roc_auc_original = auc(fpr_original, tpr_original)

# Take the square root of the scores
y_scores_sqrt = np.sqrt(y_scores)

# Calculate ROC curve for the square root of scores
fpr_sqrt, tpr_sqrt, _ = roc_curve(y_true, y_scores_sqrt)
roc_auc_sqrt = auc(fpr_sqrt, tpr_sqrt)

# Plot ROC curves
plt.figure(figsize=(8, 6))
plt.plot(fpr_original, tpr_original, color='darkorange', lw=2, label=f'Original ROC (AUC = {roc_auc_original:.2f})')
plt.plot(fpr_sqrt, tpr_sqrt, color='green', lw=2, label=f'Square Root ROC (AUC = {roc_auc_sqrt:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.show()
