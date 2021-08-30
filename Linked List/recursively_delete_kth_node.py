def deleteNode(start, k) :
 
    # If invalid k
    if (k < 1) :
        return start
 
    # If linked list is empty
    if (start == None):
        return None
 
    # Base case (start needs to be deleted)
    if (k == 1) :
     
        res = start.next
        return res
     
    start.next = deleteNode(start.next, k - 1)
    return start
 
# Utility function to insert a node
# at the beginning
def push(head_ref, new_data) :
  
    new_node = Node(0)
    new_node.data = new_data
    new_node.next = head_ref
    head_ref = new_node
    return head_ref
 
# Utility function to print a linked list
def printList( head) :
 
    while (head != None):
     
        print(head.data, end = " ")
        head = head.next
     
    print("\n")

head = None
 
head = push(head, 3)
head = push(head, 2)
head = push(head, 6)
head = push(head, 5)
head = push(head, 11)
head = push(head, 10)
head = push(head, 15)
head = push(head, 12)
     
k = 3
head = deleteNode(head, k)
 
print("Modified Linked List: ", end = "")
printList(head)