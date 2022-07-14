class Node:
    def __init__(self, value): 
        self.value = value  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.value) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
    lsit=[]
    def preorder(self,root):
        
        print(root.value)
        if root:
            print(root.val,end = ' ')
            self.preorder(root.left)
            self.preorder(root.right)
        # if root.right == None:
        #     self.preOrder(root.right)
        # else:
        #     self.preOrder(root.left)


    
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.value (the value of the node)
"""


  # Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.preorder(tree.root))  