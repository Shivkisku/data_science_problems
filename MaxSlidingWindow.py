from collections import deque

def maxSlidingWindow(A, k):
    if not A:
        return []

    max_values = []  # List to store the maximum values in each window
    window = deque()  # Deque to store indices of elements within the current window

    for i, num in enumerate(A):
        # Remove elements that are outside the current window
        while window and window[0] < i - k + 1:
            window.popleft()

        # Remove elements that are smaller than the current element
        while window and A[window[-1]] < num:
            window.pop()

        window.append(i)

        # Add the maximum value within the current window to the result list
        if i >= k - 1:
            max_values.append(A[window[0]])

    return max_values

# Example usage:
A = [2, 5, 3, 1, 4]
k = 2
result = maxSlidingWindow(A, k)
print(result)  # Output: [5, 5, 3, 4]
