class node:
    def __init__ (self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def push(self, newdata):
        newNode = node(newdata)

        newNode.next = self.head

        self.head = newNode

    def count(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        return count

    def reccount(self, node):
        if node:
            return 1 + self.reccount(node.next)
        else:
            return 0

if __name__=='__main__':
    llist = linkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
  # print('Count of nodes is :',llist.reccount(llist.head))
    print('Count of nodes is :',llist.count())
