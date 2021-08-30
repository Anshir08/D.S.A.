from insertion import linkedList

class newClass(linkedList):

    def detectloopbyhashmap(self, ):
        s = set()
        temp = self.head

        while(temp):
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next

        return False
    def detectLoop(self):
        if self.head is None:
            return 0
        slow = self.head
        fast = self.head
        flag = 0

        while(slow and slow.next and fast and
              fast.next and fast.next.next):
            if slow == fast and flag != 0:
                count = 1
                slow = slow.next
                while(slow != fast):
                    slow = slow.next
                    count += 1
                return count
             
            slow = slow.next
            fast = fast.next.next
            flag = 1
        return 0

if __name__ == '__main__':
    llist = newClass()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(10)
    
    # Create a loop for testing
    llist.head.next.next.next.next = llist.head
    
    if(llist.detectloopbyhashmap()):
        print("Loop found")
        print("Length of loop is",llist.detectLoop())
    else:
        print("No Loop ")

    