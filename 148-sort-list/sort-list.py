# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        curr = head
        while curr:
            temp.append(curr.val)
            curr = curr.next
        temp.sort()
        dummy = ListNode()
        curr = dummy
        for val in temp:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next