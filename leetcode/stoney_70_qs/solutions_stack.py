# https://leetcode.com/problems/min-stack/
class MinStack:
    # O(1) Time, O(N) Space

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            current_min = val
        else:
            current_min = min(val, self.stack[-1][1])
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


class Solution:
    # https://leetcode.com/problems/valid-parentheses/
    def isValid(self, s: str) -> bool:
        # Problem: An input string is valid if:
        # - Open brackets must be closed by the same type of brackets.
        # - Open brackets must be closed in the corrent order.

        # Solution: Append to stack if opening bracket, '([{' and if corrent the closing bracket should be
        # key in the dict, with value equal to last opening bracket in stack. If not, it will get appended
        # to stack, and final check will return a stack exists == False

        stack = []

        hashmap = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for element in s:
            if stack and (element in hashmap and stack[-1] == hashmap[element]):
                stack.pop()
            
            else:
                stack.append(element)
        
        return not stack
