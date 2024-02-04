# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        prev, curr = dummy, head
        for i in range(left-1):
            prev, curr = curr, curr.next
        
        n_prev= None

        for i in range(right-left+1):
            temp = curr.next
            curr.next = n_prev
            n_prev, curr = curr, temp
        
        prev.next.next = curr
        prev.next = n_prev
        

        return dummy.next

