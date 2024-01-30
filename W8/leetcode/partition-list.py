# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return
        # APPROCH 1
        less1 = ListNode()
        great1 = ListNode(0)
        less = less1
        great = great1
        trav = head
        add = great

        while trav:
            insert = ListNode(trav.val)
            if trav.val < x:
                less.next = insert
                less = less.next
            else:
                great.next = insert
                great = great.next

            trav = trav.next
        # print(great1)
        # print(less1)
        less.next = add.next
        return less1.next