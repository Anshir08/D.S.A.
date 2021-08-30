from insertion import linkedList,node

def modularNode(head, k):
    i = 1
    ptr = head
    res = None
    while ptr:
        if i%k == 0:
            res = ptr
        ptr = ptr.next
        i += 1
    return res

if __name__ == '__main__':
    head = node(1)
    head.next = node(2)
    head.next.next = node(3)
    head.next.next.next = node(8)
    head.next.next.next.next = node(5)
    k = 2
    answer = modularNode(head, k)
    print("Modular node is", end = ' ')
    if (answer != None):
        print(answer.data, end = ' ')
    else:
        print("None")