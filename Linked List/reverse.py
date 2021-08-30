from insertion import linkedList

class newClass(linkedList):

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def recReverse(self, head):
        
        if head is None or head.next is None:
            return head
        
        rest = self.recReverse(head.next)

        head.next.next = head
        head.next = None

        return rest

    def printrev(self, temp):
        if temp:
            self.printrev(temp.next)
            print(temp.data, end = ' ')
        else:
            return

if __name__ == '__main__':
    llist = newClass()

    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(85)
    
    print ("Given Linked List")
    llist.printList()

    # llist.reverse()

    #llist.head = llist.recReverse(llist.head)
    print ("\nReversed Linked List")
    
    # llist.printList()

    llist.printrev(llist.head)