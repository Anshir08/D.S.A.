from insertion import linkedList

class newClass(linkedList):

    def removeDuplicates(self):
        temp = self.head
        if temp is None:
            return 
        while temp.next:
            if temp.data == temp.next.data:
                temp.next = None
                temp.next = temp.next.next
            else:
                temp = temp.next
        return

if __name__ == '__main__':
    llist = newClass()

    llist.push(20)
    llist.push(13)
    llist.push(13)
    llist.push(11)
    llist.push(11)
    llist.push(11)
    print ("Created Linked List: ")
    llist.printList()
    print()
    print("Linked List after removing",
                "duplicate elements:")
    llist.removeDuplicates()
    llist.printList()