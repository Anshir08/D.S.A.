from insertion import linkedList

class newclass(linkedList):
    
    def printNthFromLast(self, n):
        temp = self.head # used temp variable
         
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
         
        if n > length:
            print('Location is greater than the' +
                         ' length of LinkedList\n')
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        print(temp.data)

l = newclass()
l.push(3)
l.push(9)
l.push(20)
l.push(4)
l.push(15)
l.push(35)
"""35 -> 15 -> 4 -> 20 -> 9 ->3"""
l.printNthFromLast(8)

