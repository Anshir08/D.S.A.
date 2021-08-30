from insertion import linkedList, node

def deleteMiddle(head):
    if head is None:
        return None
    if head.next is None:
        del head
        return None
    
    count = 0
    copyhead = head
    while copyhead:
        count += 1
        copyhead = copyhead.next

    copyhead = head
    mid = count//2

    while mid>1:
        mid-=1
        copyhead = copyhead.next

    next = copyhead.next.next
    copyhead.next = None
    copyhead.next = next

    return head

        



def printList(ptr):
 
    while (ptr != None):
        print(ptr.data, end = '->')
        ptr = ptr.next
     
    print('NULL')

if __name__=='__main__':
     
    # Start with the empty list
    head = node(1)
    head.next = node(2)
    head.next.next = node(3)
    head.next.next.next = node(4)
  
    print("Gven Linked List")
    printList(head)
  
    head = deleteMiddle(head)
  
    print("Linked List after deletion of middle")
    printList(head)