from insertion import node

def addWithCarry(head):
 
    # If linked list is empty, then
    # return carry
    if (head == None):
        return 1
 
    # Add carry returned be next node call
    res = head.data + addWithCarry(head.next)
 
    # Update data and return new carry
    head.data = int((res) % 10)
    return int((res) / 10)
 
# This function mainly uses addWithCarry().
def addOne(head):
 
    # Add 1 to linked list from end to beginning
    carry = addWithCarry(head)
 
    # If there is carry after processing all nodes,
    # then we need to add a new node to linked list
    if (carry != 0):
     
        newNode = node(0)
        newNode.data = carry
        newNode.next = head
        return newNode # New node becomes head now
     
    return head

def printList(node):
 
    while (node != None):
     
        print( node.data,end = "")
        node = node.next
     
    print("\n")   
         


# Driver's Code

#llist = linkedList()
head = node(1)
head.next = node(9)
head.next.next = node(9)
head.next.next.next = node(9)

print("List is ")
printList(head)
 
head = addOne(head)
 
print("\nResultant list is ")
printList(head)