from insertion import linkedList

class newClass(linkedList):

    def moveToFront(self):
        sec_last = None
        temp = self.head

        if not temp or not temp.next:
            return

        while temp and temp.next:
            sec_last = temp
            temp = temp.next
        
        sec_last.next = None

        temp.next = self.head
        self.head = temp

if __name__ == '__main__':
    llist = newClass()
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print ("Linked List before moving last to front ")
    llist.printList()
    llist.moveToFront()
    print()
    print ("Linked List after moving last to front ")
    llist.printList()