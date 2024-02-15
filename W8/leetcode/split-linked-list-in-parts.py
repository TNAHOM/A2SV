# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        trav = head
        size = 0

        while trav:
            trav = trav.next
            size+=1
        
        rem = size % k
        each = size//k

        curr = head
        output = []
        for x in range(k):
            output.append(curr)
            
            for y in range(each - 1 + (1 if rem else 0)):
                if not curr:
                    break
                curr = curr.next
            rem-=(1 if rem else 0)
            if curr:
                curr.next, curr = None, curr.next
        return output