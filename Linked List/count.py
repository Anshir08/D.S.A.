from insertion import linkedList

class newClass(linkedList):
    def count(self, x):
        current = self.head
        count = 0

        while current:
            if current.data == x:
                count+=1
            current = current.next
        
        return count

if __name__ == '__main__':
    llist = newClass()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    
    print("Count of 1 is ", llist.count(1))