# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # n = node()
        # 
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        x = slow
        prev = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        while prev and head:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next


        return True  
