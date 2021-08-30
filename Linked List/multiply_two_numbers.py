from insertion import linkedList, node

class newClass(linkedList):
    def multiplication(self,first, second):
        num1 = 0
        num2 = 0
        first_ptr = first.head
        second_ptr = second.head

        while first_ptr or second_ptr:
            if first_ptr:
                num1 = num1*10 + first_ptr.data
                first_ptr = first_ptr.next
            if second_ptr:
                num2 = num2*10 +second_ptr.data
                second_ptr = second_ptr.next

        return num1*num2

if __name__ == '__main__':
    first = newClass()
    second = newClass()

    first.push(6)
    first.push(4)
    first.push(9)
 
    # Printing first Linked List
    print("First list is: ", end = '')
    first.printList()
    print()
    # Create second Linked List 8->4
    second.push(4)
    second.push(8)
 
    # Printing second Linked List
    print("Second List is: ", end = '')
    second.printList()
    print()

    # Printing the result
    res = newClass()
    result = res.multiplication(first, second)
    print('Result is : ',result)