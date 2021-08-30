from insertion import linkedList

class newClass(linkedList):
    def printmiddle(self):
        count = 0
        mid = self.head
        heads = self.head

        while heads:
            if count&1:
                mid = mid.next
            count += 1
            heads = heads.next

        if mid!=None:
            print("The middle element is ", mid.data)

if __name__ == '__main__':
    llist = newClass()
    
    for i in range(5, 0, -1):
        llist.push(i)
        llist.printList()
        print()
        llist.printmiddle()
        print()