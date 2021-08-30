from insertion import linkedList, node

class newClass(linkedList):
    def middle_head(self, head):

        if head is None:
            return None
        if head.next is None:
            return head 

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        ptr = head
        while ptr.next != slow:
            ptr = ptr.next


        ptr.next = slow.next
        
        slow.next = head

        self.head = slow
# Driver's Code

ll = newClass()
ll.push(10)
ll.push(9)
ll.push(8)
ll.push(7)
ll.push(6)
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)

print("Before making middle node as head linkList was")
ll.printList()

ll.middle_head(ll.head)
print()

print("After making middle node as head linkList is ")
ll.printList()