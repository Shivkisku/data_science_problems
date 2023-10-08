import math

def calculate_mean(data):
    return sum(data) / len(data)

def calculate_correlation(X, Y):
    if len(X) != len(Y):
        raise ValueError("Lists X and Y must have the same length.")

    mean_X = calculate_mean(X)
    mean_Y = calculate_mean(Y)

    numerator = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(len(X)))
    denominator_X = math.sqrt(sum((X[i] - mean_X) ** 2 for i in range(len(X))))
    denominator_Y = math.sqrt(sum((Y[i] - mean_Y) ** 2 for i in range(len(Y))))

    correlation = numerator / (denominator_X * denominator_Y)

    return correlation

# Example data
X = [1, 2, 3, 4, 5]
Y = [2, 3, 4, 5, 6]

correlation = calculate_correlation(X, Y)
print(f"Correlation between X and Y: {correlation:.2f}")
