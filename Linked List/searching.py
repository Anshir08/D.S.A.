class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def push(self, newdata):
        newnode = node(newdata)

        newnode.next = self.head

        self.head = newnode

    def search(self, x):
        temp = self.head

        while temp:
            if temp.data == x:
                return True
            temp = temp.next
        
        return False

if __name__ == '__main__':
 
    llist = linkedList()
    
    llist.push(10);
    llist.push(30);
    llist.push(11);
    llist.push(21);
    llist.push(14);
 
    if llist.search(21):
        print("Yes")
    else:
        print("No")