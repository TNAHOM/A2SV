# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        first = head

        while curr and curr.next:

            while curr.next and curr and curr.val == curr.next.val:
                curr = curr.next

            
            curr = curr.next
            first.next = curr
            first = first.next   

        return head

        
