class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = (None)
        

    def get(self, index: int) -> int:
       
        trav = self.head
        i = 0

        while i < index and trav:
            trav = trav.next
            i+=1
       
        if not trav:
            return -1

        return trav.val

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        self.head = new
        

    def addAtTail(self, val: int) -> None:
        if not self.head:
            new = Node(val)
            self.head = new
            return

        trav = self.head

        while trav.next:
            trav = trav.next
        
        new = Node(val)
        trav.next = new

        trav = self.head


    def addAtIndex(self, index: int, val: int) -> None:
        dummy = Node(10)
        dummy.next = self.head
        trav = dummy

        i = 0
        while i < index and trav:
            trav = trav.next
            i+=1
        new = Node(val)

        if not trav:
            return 
        curr_next = trav.next 
        trav.next = new
        new.next = curr_next

        self.head = dummy.next
        
        
    def deleteAtIndex(self, index: int) -> None:
        
        if index == 0:
            self.head = self.head.next
            return
        
        trav = self.head
        i = 0
        while i < index-1 and trav:
            trav = trav.next
            i+=1
        
        if trav and trav.next:
            trav.next = trav.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)