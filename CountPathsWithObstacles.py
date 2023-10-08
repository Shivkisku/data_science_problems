def count_paths_with_obstacles(matrix):
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])

    # Create a 2D array to store the number of paths to reach each cell
    paths = [[0] * n for _ in range(m)]

    # Initialize the number of paths for the top-left cell
    paths[0][0] = 1 if matrix[0][0] == 0 else 0

    # Initialize the first row and first column
    for i in range(1, m):
        paths[i][0] = paths[i - 1][0] if matrix[i][0] == 0 else 0
    for j in range(1, n):
        paths[0][j] = paths[0][j - 1] if matrix[0][j] == 0 else 0

    # Calculate the number of paths for each cell in the matrix
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

    # Return the number of paths to the bottom right corner
    return paths[m - 1][n - 1]

# Example usage:
matrix = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 1, 0]
]
result = count_paths_with_obstacles(matrix)
print(f"The number of ways to navigate is: {result}")
