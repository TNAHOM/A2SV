# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new1 = ListNode(10)
        new = new1
        head_1 = list1
        head_2 = list2

        while head_1 and head_2:
            if head_1.val  < head_2.val:
                insert = ListNode(head_1.val)
                new.next = insert
                new = new.next
                head_1 = head_1.next
            else:
                insert = ListNode(head_2.val)
                new.next = insert
                new = new.next
                head_2 = head_2.next
        
        if head_1:
            new.next = head_1
        elif head_2:
            new.next = head_2
        
        return new1.next