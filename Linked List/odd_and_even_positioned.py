from insertion import linkedList, node

class newClass(linkedList):
    def rearrangeEvenOdd(self, head):
        if head is None: 
            return

        if head.next is None:
            return head

        odd = head
        even = head.next

        firsteven = even

        while True:
            if even.next:
                odd.next = even.next
                odd = even.next
            else:
                break
            if odd.next:
                even.next = odd.next
                even = odd.next
            else:
                break
        odd.next = firsteven
        even.next = None
        return head


        return head
    def printlist(self, node):
        while (node != None):
            print(node.data, end = "")
            print("->", end = "")
            node = node.next
        print ("NULL")


ll = newClass()
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
print ("Given Linked List")
ll.printlist(ll.head)
 
start = ll.rearrangeEvenOdd(ll.head)
 
print ("\nModified Linked List")
ll.printlist(start)