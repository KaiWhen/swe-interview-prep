from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # https://leetcode.com/problems/middle-of-the-linked-list/
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Problem: Given the head of a linked list, find the mid-point
        # Solution: Fast and Slow Pointers. O(N) Time, exploiting the fact
        # the fact the distance increases by 1 every time, when the fast pointer
        # reaches the end of the list, the slow pointer will have reached the
        # middle. Constant space.

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    

    # https://leetcode.com/problems/linked-list-cycle/
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Problem: Given the head of a linked list, determine if there is a cycle
        # Solution: Fast and Slow pointers. O(N) Time, O(1) Space. Each step, the
        # distance between the fast and the slow pointers will increase by 1, so
        # once in the loop, the distance will decrease by 1 til meet.

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
    

    # https://leetcode.com/problems/reverse-linked-list/
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(N) Time, O(1) Space.

        prev = None
        curr = self.head

        while curr != None:
            # move next pointer (right)
            next_pointer = curr.next
            
            # move link to prev (left)
            curr.next = prev

            # update curr & prev
            prev = curr
            curr = next_pointer
        
        self.head = prev
    

    # https://leetcode.com/problems/remove-linked-list-elements/
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Problem: Given the head of a linked list, and integer value, remove all nodes equal to given
        # value, and return head

        # Solution: O(N) Time, O(1) Space. Using a dummy head helps remove the need to treat head as special case,
        # and simplifies the code.

        dummy_head = ListNode(-1)
        dummy_head.next = head

        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        
        return dummy_head.next
    

    # https://leetcode.com/problems/reverse-linked-list-ii/
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Problem: Given the head of a linked list, and two ints left and right, reverse nodes of list from
        # left to right (1-indexed)
        
        # Solution: left_prev, current_node, next_pointer, previous. O(N) Time - one pass, O(1) Space.

        dummy_head = ListNode(-1, head)

        # Set up left = current node and left previous
        left_prev, current_node = dummy_head, head
        for i in range(left-1):
            left_prev, current_node = current_node, current_node.next
        
        # Traverse and reverse
        prev = None
        for i in range(right - left + 1):
            next_pointer = current_node.next
            current_node.next = prev
            prev, current_node = current_node, next_pointer
        
        # Update left prev to point to node after reversals and left node to right node
        left_prev.next.next = current_node
        left_prev.next = prev
        return dummy_head.next
