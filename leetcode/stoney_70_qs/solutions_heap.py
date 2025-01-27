import heapq
from typing import List


class Solution:
    # https://leetcode.com/problems/kth-largest-element-in-an-array/
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Problem: given an unsorted array, return kth largest element.
        
        # Solution: Can easily be done by sorted and returning index, but using
        # heap for practice.

        # using nlargest function
        # Time: O(nlog k), Space: O(k)
        return heapq.nlargest(k, nums)[-1]
    
        # heap of n size, pop k items. less efficient
        # Time: O(nlog n), Space: O(n)
        # heap = []

        # for i in nums:
        #     heapq.heappush(heap, i)
        
        # for i in range(len(nums)-k):
        #     heapq.heappop(heap)
        
        # return heapq.heappop(heap)

        # Heap of k size, return root.
        # Time: O(nlog k), Space: O(k)

        # Create a min-heap with the first k elements
        # heap = nums[:k]
        # heapq.heapify(heap) # Time complexity: O(k)

        # # Iterate through the remaining elements
        # for num in nums[k:]:
        #     if num > heap[0]:
        #         heapq.heapreplace(heap, num)
        
        # # The root of the heap is the k-th largest element
        # return heap[0] # O(1)
