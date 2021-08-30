from insertion import linkedList

class newClass(linkedList):

    def skipMdeleteN(self, m, n):
        curr = self.head
        while curr:
            for i in range(1,m):
                if curr is None:
                    return
                curr = curr.next

            if curr is None:
                return

            t = curr.next

            for i in range(1, n+1):
                if t is None:
                    break
                t = t.next
            
            curr.next = t
            curr = t


if __name__ == '__main__':
    llist = newClass()
    M = 2
    N = 3
    llist.push(0)
    llist.push(10)
    llist.push(9)
    llist.push(8)
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    
    print ("M = %d, N = %d\nGiven Linked List is:" %(M, N))
    llist.printList()
    print
    
    llist.skipMdeleteN(M, N)
    
    print ("\nLinked list after deletion is")
    llist.printList()