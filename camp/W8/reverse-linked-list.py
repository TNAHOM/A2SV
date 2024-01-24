# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trav = head
        prev = None
        new = None

        while trav:
            new = ListNode(trav.val)
            new.next = prev
            prev = new
            trav = trav.next
        
        return new
