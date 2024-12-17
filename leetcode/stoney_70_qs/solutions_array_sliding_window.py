from typing import List


class Solutions:
    # https://leetcode.com/problems/contains-duplicate-ii/
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Problem: Given an int array nums and an int k, return true if there are two distinct
        # indices i and j in the array such that nums[i] == nums[j] and abs(i-j) <= k.
        # Solution: Sliding window. O(N) Traverse given array with fixed set size and check rules
        # as you go. Space with set is O(k), with dict it's O(N)

        seen = set()

        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i-k])
        return False


    # https://leetcode.com/problems/minimum-absolute-difference/
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Problem: Given an array of distinct integers arr, find all pairs of elements with
        # the min absolute difference of any two elements
        # Solution: O(nlogn) sort and iterate through list, holding the current lowest difference
        # value in memory and updating the return list and lowest value on the fly

        # 1. Sort the array
        arr.sort()

        # 2. Find the min absolute difference
        min_diff = float('inf')
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i-1])
        
        # 3. Collect all pairs with min difference
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                result.append([arr[i-1], arr[i]])
        
        return result


    # https://leetcode.com/problems/minimum-size-subarray-sum/
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Problem: Given an array of integers arr and target, return minimal length
        # of subarray which is >=target else return 0
        
        # Solution: Sliding Window implemented via Two Pointers.
        # Time O(N), even though iterating through array twice and L and R, it is a one pass
        # linear iteration across the array of both pointers, not a compounded loop like O(N^2)
        # Space: O(1)

        l = 0
        total = 0
        res = float('inf')

        # r pointer start at 0 traverse through array
        for r in range(len(nums)):
            total += nums[r]

            # when total reaches target, get min size of subarray then move l pointer to the right
            while total >= target:
                res = min(res, r-l+1)
                total -= nums[l]
                l += 1
        
        if res == float('inf'):
            return 0
        else:
            return res
