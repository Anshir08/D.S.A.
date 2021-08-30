from insertion import node

def firstNonRepeating(head):
    mp = dict()
    temp = head

    while temp:
        if temp.data not in mp:
            mp[temp.data] = 0
        mp[temp.data] += 1
        temp = temp.next   
    
    temp = head

    while temp:
        if temp.data in mp:
            if mp[temp.data] == 1:
                return temp.data

        temp = temp.next

    return -1


def push(head_ref, new_data):
  
    new_node = node(new_data)
    new_node.next = head_ref
    head_ref = new_node
      
    return head_ref
  
# Driver code
if __name__=='__main__':
      
    # Let us create below linked list.
    # 85->15->18->20->85->35->4->20->NULL 
    head = None
    head = push(head, 20)
    head = push(head, 4)
    head = push(head, 35) 
    head = push(head, 85)  
    head = push(head, 20)
    head = push(head, 18)
    head = push(head, 15)
    head = push(head, 85)
      
    print(firstNonRepeating(head))