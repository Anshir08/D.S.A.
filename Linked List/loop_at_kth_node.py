from insertion import node

def makeloop(head, k):
    if head is None:
        return

    if head.next is None:
        return head

    while head.next:
        k -= 1
        if k==0:
            temp = head
        head = head.next
    head.next = temp

def push(head_ref, new_data):
    new_node = node(new_data)
    new_node.data = new_data
    new_node.next = head_ref
    head_ref = new_node
    return head_ref
 
# Function to print linked list
def printList( head,total_nodes):
    curr = head
    count = 0
    while (count < total_nodes):
        count = count + 1
        print(curr.data, end = " ")
        curr = curr.next
    # if curr!=None:
    #     print(curr.next.data)
    
def countNodes(ptr):
    count = 0
    while (ptr != None):
        ptr = ptr.next
        count = count + 1
     
    return count

if __name__=='__main__':
     
    # Create a linked list 1.2.3.4.5.6.7
    head = None
    head = push(head, 7)
    head = push(head, 6)
    head = push(head, 5)
    head = push(head, 4)
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
 
    # k should be less than the
    # numbers of nodes
    k = 2
    total_nodes = countNodes(head)
 
    print("Given list")
    printList(head, total_nodes)
 
    makeloop(head, k)
 
    print("\nModified list")
    printList(head, total_nodes)