from insertion import linkedList

class nayiClass(linkedList):
    def detectandremoveloop(self):
        slow = fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                self.removeloop(slow)
                return 1

        return 0

    def removeloop(self, loop_node):
        ptr1 = self.head

        while 1:
            ptr2 = loop_node
            while ptr2.next != loop_node and ptr2.next != ptr1:
                ptr2 = ptr2.next

            if ptr2.next == ptr1:
                break

            ptr1 = ptr1.next
        
        ptr2.next = None

    # optimized solution
    def detectAndRemoveLoop(self):      
 
        if self.head is None:
            return
        if self.head.next is None:
            return
 
        slow = self.head
        fast = self.head
 
        # Move slow and fast 1 and 2 steps respectively
        slow = slow.next
        fast = fast.next.next
 
        # Search for loop using slow and fast pointers
        while (fast is not None):
            if fast.next is None:
                break
            if slow == fast:
                break
            slow = slow.next
            fast = fast.next.next
 
        # if loop exists
        if slow == fast:
            slow = self.head
            while (slow.next != fast.next):
                slow = slow.next
                fast = fast.next
 
            # Sinc fast.next is the looping point
            fast.next = None  # Remove loop

llist = nayiClass()
llist.push(10)
llist.push(4)
llist.push(15)
llist.push(20)
llist.push(50)
 
# Create a loop for testing
llist.head.next.next.next.next.next = llist.head.next.next
 
llist.detectAndRemoveLoop()
 
print("Linked List after removing loop")
llist.printList()