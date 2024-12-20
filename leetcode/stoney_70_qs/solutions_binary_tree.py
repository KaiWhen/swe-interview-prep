from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/problems/average-of-levels-in-binary-tree/
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Problem: Given the root as an array of a binary tree, return the average value
        # of the nodes on each level in the form of an array.

        # Solution: BFS:
        # - O(N) time to traverse the entire tree
        # - Space is O(N), as storing in the queue grows the size of tree input. For a complete
        # binary tree, the last level can have up to (n/2) nodes, leading to a space complexity of O(n).
        # - Starting with the root in a queue, solution loops each level (BFS), removing nodes at that level
        # from the queue and appending value to level, also adding all children to queue, adding average
        # from level to result, and repeating until queue is empty (leaf nodes with no children).

        queue = deque([root])
        result = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(sum(level) / len(level))
        return result
    

    # Getting Max/Min Value in Binary Tree
    def largest_node_binary_tree(root):
        queue = deque([root])
        max_node = float('-inf')

        while queue:
            curr_node = queue.popleft()
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
            
            if curr_node.val > max_node:
                max_node = curr_node.val
        
        return max_node
    

    # https://leetcode.com/problems/binary-tree-level-order-traversal/
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Problem: Given binary tree, return left to right, level by level.
        # Solution: Breadth first search, Time O(N), Space O(N).

        if root == None:
            return []

        queue = deque([root])
        tree = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            tree.append(level)

        return tree
    

    # https://leetcode.com/problems/same-tree/
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Problem: Given the root of two binary trees, check if are same#
        # Solution: DFS - check each node for each tree, iterating down the trees depth first. Using
        # a LIFO stack, and always appending the same node first, means the loop will exhaust the left
        # (or right if you append 2nd second) subtrees first in DFS manner.

        stack = [(p,q)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            elif None in [node1, node2] or node1.val != node2.val:
                return False
            
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
        
        return True
    


    
