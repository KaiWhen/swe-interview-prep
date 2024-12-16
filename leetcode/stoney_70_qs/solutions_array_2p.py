from collections import deque
from typing import List


class Array2p:
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    def maxProfit(self, prices: List[int]) -> int:
        # Problem: Given list of numbers, find max profit by buying on any
        # day and selling on a future day.
        # Solution: Greedy Algorithm, Two Pointers: for each L, iterate R
        # across and calculate profit, when R > L, we know we have evaluated
        # all potential max profits, so move L to where R is and repeat.
        # O(N) time with left and right pointers single iteration
        # O(1) space

        l, r = 0, 1
        max_p = 0

        while r != len(prices):
            # keep L same when less than R
            if prices[l] < prices[r]:
                prof = prices[r] - prices[l]
                max_p = max(max_p, prof)
            # else move L to R
            else:
                l = r
            
            r+=1
        
        return max_p
    

    # https://leetcode.com/problems/squares-of-a-sorted-array/
    def sortedSquares_sol1(self, nums: List[int]) -> List[int]:
        # Solution 1 O(N) Split and Merge:
        # 1. Find index 0 (loop O(N)
        # 2. reverse negatives up to 0 (O(N))
        # 3. Square and merge (O(N))
        
        # edge cases
        if not nums:
            return nums
        
        if nums[0] > 0:
            return [num**2 for num in nums]
        
        # find index first positive
        m = 0
        pos = False
        for i, n in enumerate(nums):
            if n >= 0:
                pos = True
                m=i
                break
        
        # edge case if all are negative
        if not pos:
            return [num**2 for num in reversed(nums)]
        
        #A = positive nums
        #B = reversed negatives
        A,B = nums[m:], [-1*n for n in reversed(nums[:m])]

        def merge(A,B):
            a=b=0
            ret = []

            while a < len(A) and b < len(B):
                if A[a] < B[b]:
                    ret.append(A[a])
                    a+=1
                else:
                    ret.append(B[b])
                    b+=1
            
            if a < len(A):
                ret.extend(A[a:])
            else:
                ret.extend(B[b:])
            
            return [n**2 for n in ret]
        
        return merge(A,B)
    

    # https://leetcode.com/problems/squares-of-a-sorted-array/
    def sortedSquares_sol2(self, nums: List[int]) -> List[int]:
        # Solution 2 O(N) Absolute and Merge:
        # 1. Iterate through list (O(N))
        # 2. Append to deque (O(1))

        ans = deque()
        l, r = 0, len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                ans.appendleft(left*left)
                l+=1
            else:
                ans.appendleft(right*right)
                r-=1
        return list(ans)


    # https://leetcode.com/problems/longest-mountain-in-array/
    def longestMountain(self, arr: List[int]) -> int:
        # Problem: given an array, a mountain is composed of at least 3
        # integers, with an increase and decrease. Find the longest mountain
        # Solution: Two pointers. Find the peak and send out two pointers.
        # O(N)-Average O(N^2)-Worst-case, O(1) Space
        ans = 0

        # start at idx 1 because we are searching the peak
        for i in range(1, len(arr)-1):

            if arr[i-1] < arr[i] > arr[i+1]:
                l=r=i

                while l>0 and arr[l] > arr[l-1]:
                    l-=1
                    print(l)
                
                while r<len(arr)-1 and arr[r] > arr[r+1]:
                    r+=1
                    print(r)
                
                ans = max(ans, r-l+1)
        
        return ans
