# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # set up two pointers, l, r
        if not head:
            return False
        l = head
        r = head.next
        while l != r:

            if r:
                r = r.next
            if r:
                r = r.next
            else:
                return False
            
            l = l.next

        return True