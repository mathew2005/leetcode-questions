# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        dumNode = ListNode()
        curr = dumNode
        while ptr1 or ptr2:
            # ptr1.val > ptr2.val
            if ptr1 and not ptr2:
                curr.next = ptr1
                break
            if not ptr1 and ptr2:
                curr.next = ptr2
                break
            if ptr1.val >= ptr2.val:
                curr.next = ListNode()
                curr = curr.next
                curr.val = ptr2.val
                ptr2 = ptr2.next
            else:
                curr.next = ListNode()
                curr = curr.next
                curr.val = ptr1.val
                ptr1 = ptr1.next

        return dumNode.next