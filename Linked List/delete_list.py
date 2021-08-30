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

    def deleteList(self):
        print("\nLinked list deleting...")
        current = self.head
        
        while current:
            del current.data
            current = current.next
            
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
    llist.deleteList()
    print("\nLinked list deleted")