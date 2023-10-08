import numpy as np

def ndcg_at_k(ranking, k):
    # Calculate Discounted Cumulative Gain (DCG) at position k
    dcg = np.sum((2 ** np.array(ranking) - 1) / np.log2(np.arange(2, k + 2)))

    # Calculate Ideal Discounted Cumulative Gain (IDCG) at position k (perfect ranking)
    ideal_ranking = np.sort(ranking)[::-1]
    idcg = np.sum((2 ** ideal_ranking - 1) / np.log2(np.arange(2, k + 2)))

    # Calculate NDCG at position k
    ndcg = dcg / idcg if idcg > 0 else 0.0
    return ndcg

# Example usage:
user_ranking = [2, 3, 1, 4, 5]  # User's ranked list of shows
k = 5  # Evaluate NDCG at position 5

ndcg = ndcg_at_k(user_ranking, k)
print(f"NDCG at position {k}: {ndcg:.4f}")
