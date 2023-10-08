# MaxIncreasingSubsequenceSum.py

def max_increasing_subsequence_sum(nums):
    if not nums:
        return 0

    n = len(nums)
    max_sum = [0] * n

    for i in range(n):
        max_sum[i] = nums[i]

        for j in range(i):
            if nums[i] > nums[j]:
                max_sum[i] = max(max_sum[i], max_sum[j] + nums[i])

    return max(max_sum)

# Examples
input1 = [5, 4, 3, 2, 1]
input2 = [3, 2, 5, 7, 6]

result1 = max_increasing_subsequence_sum(input1)
result2 = max_increasing_subsequence_sum(input2)

print(f"Result 1: {result1}")  # Output: 5
print(f"Result 2: {result2}")  # Output: 15
