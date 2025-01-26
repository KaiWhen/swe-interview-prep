### Maximum Subarray Sum - Kadane's Algorithm (Medium)

Time Complexity: O(n)
Space Complexity: O(1)

```py
def maxSubArray(self, nums: List[int]) -> int:
    maxSub, curSum = nums[0], 0
    for num in nums:
        if curSum < 0:
            curSum = 0
        curSum += num
        maxSub = max(maxSub, curSum)
    return maxSub
```