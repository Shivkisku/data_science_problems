# MedianFinder.py

import heapq

class MedianFinder:
    def __init__(self):
        # Max-heap to store the left half of the elements
        self.left_heap = []  # Use negation for max-heap behavior
        # Min-heap to store the right half of the elements
        self.right_heap = []

    def addNum(self, num):
        # Add the number to one of the heaps and balance the heaps
        if not self.left_heap or num <= -self.left_heap[0]:
            heapq.heappush(self.left_heap, -num)
        else:
            heapq.heappush(self.right_heap, num)

        # Balance the heaps if necessary
        if len(self.left_heap) > len(self.right_heap) + 1:
            heapq.heappush(self.right_heap, -heapq.heappop(self.left_heap))
        elif len(self.right_heap) > len(self.left_heap):
            heapq.heappush(self.left_heap, -heapq.heappop(self.right_heap))

    def findMedian(self):
        # If the number of elements is odd, the median is the top of the left heap
        if len(self.left_heap) > len(self.right_heap):
            return -self.left_heap[0]
        # If the number of elements is even, the median is the average of the tops of both heaps
        else:
            return (-self.left_heap[0] + self.right_heap[0]) / 2.0

# Example usage:
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())  # Output: 1.5
medianFinder.addNum(3)
print(medianFinder.findMedian())  # Output: 2.0
