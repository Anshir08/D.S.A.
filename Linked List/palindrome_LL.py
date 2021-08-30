from insertion import linkedList

class newClass(linkedList):

    def ispalindrome_stack(self):
        slow = self.head
        stack = []

        while slow:
            stack.append(slow.data)
            slow = slow.next

        slow = self.head

        while slow:
            i = stack.pop()

            if i!=slow.data:
                return False
            slow = slow.next

        return True


if __name__ == '__main__':
    llist = newClass()
    llist.push(1)
    llist.push(2)
    llist.push('a')
    llist.push('b')
    llist.push(2)
    llist.push(1)

    if llist.ispalindrome_stack():
        print('yess this a fucking palindrome')
    else:
        print("Oooo no, it's not")