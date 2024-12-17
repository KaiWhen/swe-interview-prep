from typing import List


class Solution:
    # https://leetcode.com/problems/single-number/
    def singleNumber(self, nums: List[int]) -> int:
        # Problem: Every element appears twice except for one. Find it.
        # Solution: XOR of any two num gives the difference of bit as 1 and same bit as 0.
        # Thus, using this we get 1 ^ 1 == 0

        xor = 0
        for i in nums:
            xor ^= i
        
        return xor