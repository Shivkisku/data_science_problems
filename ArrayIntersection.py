def intersection(A, B):
    set_A = set(A)
    set_B = set(B)
    result = set_A.intersection(set_B)
    return list(result)

# Example usage:
A = [2, 4, 1, 5, 0]
B = [3, 4, 5]
result = intersection(A, B)
print(result)
