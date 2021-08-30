from insertion import linkedList, node

def mergeLists(head1, head2):
    dummyNode = node(0)
    tail = dummyNode

    while True:

        if head1 is None:
            tail.next = head2
            break
        if head2 is None:
            tail.next = head1
            break

        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next

    return dummyNode.next



listA = linkedList()
listB = linkedList()
 
# Add elements to the list in sorted order
listA.append(5)
listA.append(10)
listA.append(15)
 
listB.append(2)
listB.append(3)
listB.append(20)
 
# Call the merge function
listA.head = mergeLists(listA.head, listB.head)
 
# Display merged list
print("Merged Linked List is:")
listA.printList()