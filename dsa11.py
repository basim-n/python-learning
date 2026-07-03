class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node=TreeNode(value)
        if self.root==None:
            self.root=new_node 
            return # if tree is empty, new node becomes root
         

        current=self.root
        while current is not None:
            if new_node.value<current.value:
                if current.left is None:
                    current.left=new_node
                    return
                else:
                    current=current.left
            elif new_node.value>current.value:

                if current.right is None:
                    current.right=new_node
                    return
                else:
                    current=current.right
            
            # otherwise find the correct position
        # left if smaller, right if larger
    
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)

    def search(self, value):
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False
    

bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)

bst.inorder(bst.root)    # should print 3 5 7 10 15
print(bst.search(7))     # True
print(bst.search(99))    # False