from insertion import linkedList, node

class newClass(linkedList):
    def sortList(self):
        count = [0,0,0]

        ptr = self.head

        while ptr:
            count[ptr.data] += 1
            ptr = ptr.next

        i = 0
        ptr = self.head

        while ptr:
            if count[i] == 0:
                i += 1
            else:
                ptr.data = i
                count[i] -= 1
                ptr = ptr.next
        

llist = newClass()
llist.push(0)
llist.push(1)
llist.push(0)
llist.push(2)
llist.push(1)
llist.push(1)
llist.push(2)
llist.push(1)
llist.push(2)
 
print("Linked List before sorting")
llist.printList()
 
llist.sortList()
 
print("Linked List after sorting")
llist.printList()