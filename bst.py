class Node:
    def __init__(self, info):
        self.value = value  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.value) 

def preOrder(root):
    if root == None:
        return
    print (root.value, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.value (the value of the node)

    def insert(self, root ,val):
        #Enter you code here.
        if root==None:
            root.value = val
        elif root.left<val:
            self.insert(root.left,val)
        elif root.right<val:
            self.insert(root.right,val)

            
        

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)