
from collections import deque


# https://leetcode.com/problems/implement-stack-using-queues/
class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for _ in range(len(self.stack)-1):
            self.stack.append(self.stack.popleft())
        
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack
