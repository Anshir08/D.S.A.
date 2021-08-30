from insertion import node

def push(head_ref, newdata):
    new_node = node(newdata)
    new_node.data = newdata
    new_node.next = head_ref
    head_ref = new_node
    return head_ref

def prList(node):
    while (node != None):
        print(node.data, end = " ")
        node = node.next

def deleteAlt(head):
    if head is None:
        return
    prev = head
    now = head.next

    while prev and now:
        prev.next = now.next
        now = None

        prev = prev.next
        if prev != None:
            now = prev.next

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

print("List before calling deleteAlt() ")
prList(head)

deleteAlt(head)

print("\nList after calling deleteAlt() ")
prList(head)