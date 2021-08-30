from insertion import linkedList, node

class newClass(linkedList):
    def identical(self, listB):
        a = self.head
        b = listB.head

        while a!=None and b!=None:
            if a.data != b.data:
                return False

            a = a.next
            b = b.next

        return (a==None and b==None)

list1 = newClass()
list2 = newClass()

list1.push(1)
list1.push(2)
list1.push(3)
list2.push(1)
list2.push(2)
list2.push(3)

if list1.identical(list2) == True:
    print("Lists are identical")
else:
    print("Lists are not identical")