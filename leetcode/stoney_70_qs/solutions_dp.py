from typing import List


class Solution:
    # https://leetcode.com/problems/coin-change/
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Problem: You are given int array coins. Return smallest number of coins to make amount.
        # Solution: Use dp, start at a target of 0 and get the min amount needed for each target up to amount.

        # fill array of size amount+1 with amount+1
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        # array idx
        for i in range(1, amount+1):
            for c in coins:
                if(i-c) >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        
        return dp[amount] if (dp[amount] != amount+1) else -1
    

    # https://leetcode.com/problems/climbing-stairs/
    def climbStairs(self, n: int) -> int:
        # Problem: How many unique ways to climb to the top of n stairs taking either 1 or 2 steps.

        # Solution: DP, Bottom-up. Move pointers one and two representing steps you can take from current
        # position, and sum values in current position.
        # Time: O(N), one iteration in range(n-1). Space: O(N) to maintain array but can be done with constant space.

        if n == 1:
            return 1

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] # Add the previous two to get the no of ways to get to ith step
        
        return dp[n]
    

    # https://leetcode.com/problems/maximum-subarray/
    def maxSubArray(self, nums: List[int]) -> int:
        # Problem: Given list of numbers, find max subarray, return sum.
        
        # Solution: O(N) Time: Sliding Window - DP
        # O(N) Space

        dp = [0] * len(nums)

        for i, n in enumerate(nums):
            dp[i] = max(n, dp[i-1]+n)
        
        return max(dp)

        # Solution with no dp, O(1) Space

        # maxSum = arr[0]
        # currentSum = 0

        # for n in arr:
        #     if currentSum < 0:
        #         currentSum = 0
            
        #     currentSum += n
        #     maxSum = max(maxSum, currentSum)
        
        # return maxSum
    

    # https://leetcode.com/problems/counting-bits/
    def countBits(self, n: int) -> List[int]:
        # Problem: Given int n, return array of length n+1, such that for
        # each i, ans[i] is the no of 1's in the binary representation of i
        
        # Solution: O(N), the no of 1's=(1 + dp [n-significant bit]).
        # The most significant bit represents every time a new column is
        # in play, 2, 4, 8, 16...

        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            # if number is equal to significant bit
            if offset*2 == i:
                offset = i
            
            dp[i] = 1 + dp[i-offset]
        
        return dp
    

# https://leetcode.com/problems/range-sum-query-immutable/
class NumArray:
    # Problem: Given list of numbers, initialize for loop up and create
    # function which sums based on given indices subrange.

    # Solution 1: O(N) Time

    # def __init__(self, nums: List[int]):
    #     self.nums = nums

    # def sumRange(self, left: int, right: int) -> int:
    #     return sum(self.nums[left:right+1])

    # Solution 2: DP, by creating a cumulative list where O(N) and
    # subtracting the value of right index but cumulative value of left
    # index O(1)

    def __init__(self, nums: List[int]):
        self.acc_nums = [0]

        for num in nums:
            self.acc_nums.append(self.acc_nums[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.acc_nums[right+1] - self.acc_nums[left]
