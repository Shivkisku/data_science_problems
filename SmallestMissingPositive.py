def firstMissingPositive(nums):
    n = len(nums)

    # Rearrange the elements to their correct positions
    for i in range(n):
        while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    # Find the first index where the element does not match its position + 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # If all positive integers from 1 to n are present, return n + 1
    return n + 1

# Example usage:
A = [1, 3, 6, 2, 7]
result = firstMissingPositive(A)
print(f"The smallest missing positive integer is: {result}")
