# FindPeakElement.py

def find_peak_element(nums):
    n = len(nums)
    
    if n == 1:
        return 0  # There's only one element, and it's a peak.
    
    # Check the first element
    if nums[0] > nums[1]:
        return 0
    
    # Check the last element
    if nums[n - 1] > nums[n - 2]:
        return n - 1
    
    # Check elements in the middle
    for i in range(1, n - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i
    
    return -1  # No peak element found

# Example usage:
A = [3, 5, 2, 4, 1]
peak_index = find_peak_element(A)
if peak_index != -1:
    print(f"The peak element is {A[peak_index]} at index {peak_index}")
else:
    print("No peak element found in the array.")
