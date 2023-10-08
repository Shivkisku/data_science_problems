from collections import defaultdict, deque

def find_smallest_number_of_friendships(graph, start_user, end_user):
    if start_user == end_user:
        return 0  # If the start and end users are the same, they are already friends.

    visited = set()
    queue = deque([(start_user, 0)])  # Initialize the queue with the start user and a distance of 0.

    while queue:
        current_user, distance = queue.popleft()
        visited.add(current_user)

        # Check if we have reached the end user.
        if current_user == end_user:
            return distance

        # Explore the friends of the current user.
        for friend in graph[current_user]:
            if friend not in visited:
                queue.append((friend, distance + 1))

    # If we couldn't reach the end user, return -1 (indicating no direct or indirect friendship).
    return -1

# Example usage:
if __name__ == "__main__":
    # Create a sample social graph as a dictionary of lists (adjacency list).
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A'],
        'D': ['B', 'E'],
        'E': ['D']
    }

    start_user = 'A'
    end_user = 'E'

    result = find_smallest_number_of_friendships(graph, start_user, end_user)
    if result != -1:
        print(f"The smallest number of friendships between {start_user} and {end_user} is {result}.")
    else:
        print(f"{start_user} and {end_user} are not connected.")
