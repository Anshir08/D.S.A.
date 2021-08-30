class BST():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def add_child(self, value):
        if value == self.value:
            return
        
        if value < self.value:
            if self.left:
                self.left.add_child(value)
            else:
                self.left = BST(value)
        else:
            if self.right:
                self.right.add_child(value)
            else:
                self.right = BST(value)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.value)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        elements.append(self.value)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
 
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.value)

        return elements

    def search(self, value):
        if value == self.value:
            return True
        
        if value < self.value:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.value

        #return tree.in_order_traversal()[0]

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.value

        #return tree.in_order_traversal()[-1]

    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.value = min_val
            self.right = self.right.delete(min_val)
        
        return self

def build_tree(elements):
    root = BST(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root
            
# Driver's Code
if __name__ == '__main__':
    arr = [12, 15, 7, 14, 27, 20, 23, 14, 88]
    strings = ['Anshir', 'is', 'sexiest', 'Human', 'on', 'the', 'Earth']
    tree = build_tree(arr)
    # print(tree.search(123))
    # print(tree.in_order_traversal())
    # print(tree.pre_order_traversal())
    # print(tree.post_order_traversal())
    # print(tree.find_max())
    # print(tree.find_min())
    # print(sum(arr))

    # tree.delete(12)
    # print(tree.in_order_traversal())
    # # print(tree.pre_order_traversal())
    # # print(tree.post_order_traversal())

    # tree.delete(7)
    # print(tree.in_order_traversal())