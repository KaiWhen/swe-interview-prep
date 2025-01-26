### Daily Temperatures - Monotonic Stack (Medium)
https://leetcode.com/problems/daily-temperatures/

Time Complexity: O(n)
Space Complexity: O(n)

```py
def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    stack = [] # pair: [temp, index]
    res = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = (i - stackInd)
        stack.append([t,i])
    return res
```