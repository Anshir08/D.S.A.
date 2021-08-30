from insertion import linkedList, node

def push(head_ref, newdata):
    new_node = node(newdata)
    new_node.data = newdata
    new_node.next = head_ref
    head_ref = new_node
    return head_ref

def printAlternate(Node, isOdd):
    if Node is None:
        return
    if isOdd == True:
        print(Node.data, end=' ')
        isOdd = False
    else:
        isOdd = True
    printAlternate(Node.next, isOdd)


head = None
head = push(head, 10)
head = push(head, 9)
head = push(head, 8)
head = push(head, 7)
head = push(head, 6)
head = push(head, 5)
head = push(head, 4)
head = push(head, 3)
head = push(head, 2)
head = push(head, 1)
 
printAlternate(head, True)