# TopicGroupCount.py

def num_topic_groups(adjacency_matrix):
    def dfs(node):
        visited[node] = True
        for neighbor in range(n):
            if adjacency_matrix[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    n = len(adjacency_matrix)
    visited = [False] * n
    num_groups = 0

    for node in range(n):
        if not visited[node]:
            dfs(node)
            num_groups += 1

    return num_groups

# Example usage:
adjacency_matrix = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
]

groups = num_topic_groups(adjacency_matrix)
print(f"There are {groups} topic groups.")
