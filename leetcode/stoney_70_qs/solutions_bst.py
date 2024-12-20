from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode.com/problems/search-in-a-binary-search-tree/
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Due to structure of BST, easy linear search O(N), with O(1) Space.

        while root:
            if root.val == val:
                return root
            
            elif root.val < val:
                root = root.right
            
            else:
                root = root.left
        
        return None


    # https://leetcode.com/problems/insert-into-a-binary-search-tree/
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Problem: Given a BST, insert given node into the tree. No duplicates.

        # Solution: Traverse the BST going down left or right subtree based on node values,
        # at some point inserted node will be less or greater than a node which does not have
        # a left or right child, and then insert.
        # Time: O(N) - N is height of tree
        # Space: O(1)

        new_node = TreeNode(val)

        if not root:
            return new_node
        
        current = root
        while True:
            if val < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    break
        
        return root
    



