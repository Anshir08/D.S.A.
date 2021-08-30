from insertion import linkedList, node

def prList(node):
    while (node != None):
        print(node.data, end = " ")
        node = node.next
    

def reverse(head):
    ptr = head
    while ptr:
        ptr.data = (ptr.data)[::-1]
        ptr = ptr.next
    return head

head = node("Geeksforgeeks") 
head.next = node("a") 
head.next.next = node("computer") 
head.next.next.next = node("science") 
head.next.next.next.next = node("portal") 
head.next.next.next.next.next = node("for") 
head.next.next.next.next.next.next = node("geeks") 
  
print( "List before reverse: ") 
prList(head) 
  
head = reverse(head) 
  
print( "\n\nList after reverse: ") 
prList(head)