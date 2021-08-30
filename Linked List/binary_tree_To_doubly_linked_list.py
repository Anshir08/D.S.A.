class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
     
    if root is not None:
        inorder(root.left)
        print("\t%d" %(root.data)),
        inorder(root.right)
 
# Changes left pointers to work as previous pointers
# in converted DLL
# The function simply does inorder traversal of
# Binary Tree and updates
# left pointer using previously visited node
def fixPrevPtr(root):
    if root is not None:
        fixPrevPtr(root.left)
        root.left = fixPrevPtr.pre
        fixPrevPtr.pre = root
        fixPrevPtr(root.right)
 
# Changes right pointers to work as nexr pointers in
# converted DLL
def fixNextPtr(root):
 
    prev = None
    # Find the right most node in BT or last node in DLL
    while(root and root.right != None):
        root = root.right
 
    # Start from the rightmost node, traverse back using
    # left pointers
    # While traversing, change right pointer of nodes
    while(root and root.left != None):
        prev = root
        root = root.left
        root.right = prev
 
    # The leftmost node is head of linked list, return it
    return root
 
# The main function that converts BST to DLL and returns
# head of DLL
def BTToDLL(root):
     
    # Set the previous pointer
    fixPrevPtr(root)
 
    # Set the next pointer and return head of DLL
    return fixNextPtr(root)
 
# Traversses the DLL from left to right
def printList(root):
    while(root != None):
        print("\t%d" %(root.data)),
        root = root.right
 
# Driver program to test above function
root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)
 
print("\n\t\t Inorder Tree Traversal\n")
inorder(root)
 
# Static variable pre for function fixPrevPtr
fixPrevPtr.pre = None
head = BTToDLL(root)
 
print("\n\n\t\tDLL Traversal\n")
printList(head)