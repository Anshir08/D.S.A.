from insertion import linkedList, node

class newClass(linkedList):

    def deleteNode(self, position):
        if self.head is None:
            return

        temp = self.head
        
        if position == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(position-1):
            temp = temp.next
            if temp is None:
                break

        if temp is None or temp.next is None:
            return 

        next = temp.next.next

        temp.next = None

        temp.next = next

    def delNode(self, node_ptr):
        temp = node_ptr.next
        node_ptr.data = temp.data
        node_ptr.next = temp.next

        
llist = newClass()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)
 
print ("Created Linked List: ")
llist.printList()
llist.deleteNode(0)
llist.delNode(llist.head) # deleting node without using pointer
print ("\nLinked List after Deletion: ")
llist.printList()