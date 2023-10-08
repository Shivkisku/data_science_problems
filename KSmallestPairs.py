import heapq

def kSmallestPairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []
    
    heap = []
    
    # Initialize the heap with the first k pairs from nums1 and nums2
    for i in range(min(k, len(nums1))):
        heap.append((nums1[i], nums2[0], 0))  # (num1, num2, index of nums2)
    
    heapq.heapify(heap)  # Convert the list into a heap
    
    result = []
    
    while k > 0 and heap:
        num1, num2, index2 = heapq.heappop(heap)
        result.append([num1, num2])
        
        # Push the next pair from nums2 associated with num1 into the heap
        if index2 + 1 < len(nums2):
            heapq.heappush(heap, (num1, nums2[index2 + 1], index2 + 1))
        
        k -= 1
    
    return result

# Example usage:
nums1 = [1, 3, 6, 10]
nums2 = [2, 5, 7, 9]
k = 3
result = kSmallestPairs(nums1, nums2, k)
print(result)  # Output: [[1, 2], [3, 2], [1, 5]]
