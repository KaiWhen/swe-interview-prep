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