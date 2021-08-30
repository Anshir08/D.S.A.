class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def push(self, newdata):
        newNode = node(newdata)

        newNode.next = self.head

        self.head = newNode

    def getNth(self, index):
        current = self.head
        count = 0

        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1


if __name__ == '__main__':
 
    llist = linkedList()
 
    # Use push() to construct below list
    # 1->12->1->4->1
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)
 
    n = 3
    print("Element at index 3 is :", llist.getNth(n))