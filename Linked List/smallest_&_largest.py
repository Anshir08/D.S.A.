from insertion import linkedList, node

class newClass(linkedList):
    def smallest_Largest(self,head):
        small = head.data
        large = head.data
        while head:
            if head.data > large:
                large = head.data
            if head.data < small:
                small = head.data
            head = head.next

        return [large,small]

if __name__ == '__main__':
    ll = newClass()
    ll.push(1)
    ll.push(11)
    ll.push(9)
    ll.push(0)
    ll.push(-1)
    ll.push(100)
    res = ll.smallest_Largest(ll.head)
    print(f"The largest no. of the LinkedList is {res[0]}\nand the smallest no. of the list is {res[1]}")