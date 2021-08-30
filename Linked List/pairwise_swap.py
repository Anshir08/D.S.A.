from insertion import linkedList

class newClass(linkedList):

    def pairwiseSwap(self):
        if self.head is None:
            return

        temp = self.head

        while temp and temp.next:
            if temp.data != temp.next.data:
                temp.data, temp.next.data = temp.next.data, temp.data

            temp = temp.next.next

if __name__ == '__main__':
    llist = newClass()
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    
    print ("Linked list before calling pairWiseSwap() ")
    llist.printList()
    
    llist.pairwiseSwap()
    
    print ("\nLinked list after calling pairWiseSwap()")
    llist.printList()