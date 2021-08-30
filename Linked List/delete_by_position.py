class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def push(self, newdata):
        newNode = node(newdata)

        newNode.next = self.head

        self.head = newNode

    def delete_position(self, position):
        temp = self.head

        if temp is None:
            return 
        
        if position==0:
            self.head = temp.next
            temp = None
            return
            
        for i in range(position):
            prev = temp
            temp = temp.next
        
        if temp is None or prev is None:
            return

        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
    
        while (temp):
            print(temp.data, end=' ')
            temp = temp.next

if __name__ == '__main__':
    llist = linkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    
    print ("Created Linked List: ")
    llist.printList()
    llist.delete_position(0)
    print ("\nLinked List after Deletion:")
    llist.printList()