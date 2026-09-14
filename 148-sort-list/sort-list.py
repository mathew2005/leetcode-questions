# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # MAKE THIS RECURSIVE
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # progressivley half the linked list
            # find the middle
            if not head or not head.next: 
                return head
            # mid = self.middle(head)
            right = self.sortList(self.middle(head))
            left = self.sortList(head)

            return self.merge(left, right)


        # sort while merging as we go (when building back up)
            # sort two linked list parts
            # merge them together

    def middle(self, head):
        slowPtr = head
        fastPtr = head.next
        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
        mid = slowPtr.next
        slowPtr.next = None
        return mid


    def merge(self,list1,list2):
        dummy = tail = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        return dummy.next

