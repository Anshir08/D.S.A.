class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.rear = self.front = None

    def isEmpty(self):
        return self.front == None

    def EnQueue(self, item):
        temp = Node(item)
        if self.rear == None:
            self.rear = self.front = temp
            return
        self.rear.next = temp
        self.rear = temp

    def DeQueue(self):
        if self.isEmpty():
            return
        self.front = self.front.next
        if self.front == None:
            self.rear = None

# Driver's code

Q = Queue()
Q.EnQueue(10)
Q.EnQueue(20)
Q.DeQueue()
Q.DeQueue()
Q.EnQueue(30)
Q.EnQueue(40)
Q.EnQueue(50)
Q.DeQueue()
print(f"Front item : {Q.front.data}")
print(f"Rear item : {Q.rear.data}")