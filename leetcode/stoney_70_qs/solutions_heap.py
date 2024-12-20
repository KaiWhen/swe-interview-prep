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


# def solution(D, T):
#     n = len(D)
#     travel_times = [0] * (n+1)
#     trash_hash = {'P': 0, 'G': 1, 'M': 2}
#     truck_times = [0,0,0]

#     for i in range(1, n+1):
#         travel_times[i] = travel_times[i-1] + D[i-1]
    
#     for trash, truck in trash_hash.items():
#         furthest_house = -1
#         total_loading_time = 0

#         for i in range(n):
#             if trash in T[i]:
#                 furthest_house = i
#                 total_loading_time += T[i].count(trash)
        
#         if furthest_house != -1:
#             truck_times[truck] = (travel_times[furthest_house+1]*2) + total_loading_time
    
#     return max(truck_times)


# def solution2(S):
#     stack = []
#     prev_idx = -1
#     ans = 0

#     for i, c in enumerate(S):
#         while stack and stack[-1][1] < prev_idx:
#             stack.pop()
        
#         if stack and stack[-1][0] == c:
#             start_idx = stack[-1][1]
#             if start_idx >= prev_idx:
#                 ans += 1
#                 prev_idx = i
#                 stack.pop()
        
#         stack.append((c, i))
    
#     return ans

# def sol(S):
#     first_occurrence = {}
#     last_occurrence = {}

#     for i, char in enumerate(S):
#         if char not in first_occurrence:
#             first_occurrence[char] = i
#         last_occurrence[char] = i

#     substrings = []

#     for char in first_occurrence:
#         if last_occurrence[char] - first_occurrence[char] >= 1:
#             substrings.append((first_occurrence[char], last_occurrence[char]))

#     substrings.sort(key=lambda x: x[1])

#     count = 0
#     last_end = -1

#     for start, end in substrings:
#         if start > last_end:
#             count += 1
#             last_end = end

#     return count


# def solawefaewf(S):
#     hash_first = {}
#     hash_second = {}
#     ans = 0

#     for i, c in enumerate(S):
#         if c not in hash_first and c not in hash_second:
#             hash_first[c] = i
#         elif c in hash_first and c not in hash_second:
#             hash_second[c] = i
    
#     last_used_idx = -1
#     for i, c in enumerate(S):
#         if c in hash_first and c in hash_second and i > last_used_idx:
#             ans += 1
#             last_used_idx = hash_second[c]
    
#     return ans

        