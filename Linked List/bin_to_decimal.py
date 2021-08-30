from insertion import linkedList, node

class newClass(linkedList):
    def binaryToDecimal(self, head):
        res = 0

        while head:

            res = (res << 1) + head.data

            head = head.next

        return res

if __name__ == '__main__':
 
    #Start with the empty list
    llist = newClass()
 
    llist.head = node(1)
    llist.head.next = node(0)
    llist.head.next.next = node(1)
    llist.head.next.next.next = node(1)
     
    print("Decimal Value is {}".format(
           llist.binaryToDecimal(llist.head)))