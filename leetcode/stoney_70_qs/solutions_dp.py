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
