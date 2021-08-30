class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=' ')
            temp = temp.next

if __name__ == '__main__':
    llist = linkedList()

    llist.head = node(1)

    llist.head.next = node(2)

    llist.head.next.next = node(3)
    
    llist.printList()